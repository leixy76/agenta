// @ts-nocheck
import {useEffect, useMemo, useState} from "react"

import {CaretDown, Play} from "@phosphor-icons/react"
import {Button, Col, Dropdown, MenuProps, Modal, Row, Spin, message} from "antd"
import isEqual from "lodash/isEqual"
import dynamic from "next/dynamic"
import {useRouter} from "next/router"

import EvaluationErrorModal from "@/oss/components/Evaluations/EvaluationErrorModal"
import {useAppTheme} from "@/oss/components/Layout/ThemeContextProvider"
import {useAppsData} from "@/oss/contexts/app.context"
import {PERMISSION_ERR_MSG} from "@/oss/lib/api/assets/axiosConfig"
import {EvaluationType} from "@/oss/lib/enums"
import {getErrorMessage} from "@/oss/lib/helpers/errorHandler"
import {isDemo} from "@/oss/lib/helpers/utils"
import {getAllVariantParameters, groupVariantsByParent} from "@/oss/lib/helpers/variantHelper"
import {useVariants} from "@/oss/lib/hooks/useVariants"
import type {GenericObject, Parameter, Variant, StyleProps} from "@/oss/lib/Types"
import {createNewEvaluation} from "@/oss/services/human-evaluations/api"
import {useLoadTestsetsList} from "@/oss/services/testsets/api"

import VariantDetailsWithStatus from "../VariantDetailsWithStatus"

import {useStyles} from "./assets/styles"
import type {HumanEvaluationModalProps} from "./types"

const ShareEvaluationModal = dynamic(
    () => import("@/oss/components/Evaluations/ShareEvaluationModal"),
    {ssr: false},
)

const HumanEvaluationModal = ({
    isEvalModalOpen,
    setIsEvalModalOpen,
    evaluationType,
}: HumanEvaluationModalProps) => {
    const router = useRouter()
    const {appTheme} = useAppTheme()
    const {currentApp} = useAppsData()
    const [isError, setIsError] = useState<boolean | string>(false)
    const classes = useStyles({themeMode: appTheme} as StyleProps)

    const [selectedTestset, setSelectedTestset] = useState<{
        _id?: string
        name: string
    }>({name: "Select a Test set"})
    const [testsetsList, setTestsetsList] = useState<any[]>([])

    const [selectedVariants, setSelectedVariants] = useState<Variant[]>(
        new Array(1).fill({variantName: "Select a variant"}),
    )

    const [_selectedCustomEvaluationID, _setSelectedCustomEvaluationID] = useState("")

    const appId = router.query.app_id?.toString() || ""

    const {testsets, isTestsetsLoadingError} = useLoadTestsetsList()

    const [variantsInputs, setVariantsInputs] = useState<Record<string, string[]>>({})

    const [error, setError] = useState({message: "", btnText: "", endpoint: ""})

    const [shareModalOpen, setShareModalOpen] = useState(false)

    const {data, isLoading: areAppVariantsLoading} = useVariants(currentApp)({
        appId: currentApp?.app_id,
    })

    const variants = useMemo(() => groupVariantsByParent(data?.variants || [], true), [data])

    useEffect(() => {
        if (variants.length > 0) {
            const fetchAndSetSchema = async () => {
                try {
                    const isNewVariant = true
                    let results: {
                        variantName: string
                        inputs: string[]
                    }[]

                    const isCustom = variants.some((v) => v.isCustom)

                    if (isCustom) {
                        results = variants.map((_variant) => {
                            const variant = _variant.revisions.sort(
                                (a, b) => b.updatedAtTimestamp - a.updatedAtTimestamp,
                            )[0]
                            return {
                                variantName: variant.variantName,
                                inputs: (variant.inputParams || []).map(
                                    (ip) => ip.name || ip.title,
                                ),
                            }
                        })
                    } else if (isNewVariant) {
                        results = variants.map((_variant) => {
                            const variant = _variant.revisions.sort(
                                (a, b) => b.updatedAtTimestamp - a.updatedAtTimestamp,
                            )[0]
                            return {
                                variantName: variant.variantName,
                                inputs: (variant.inputParams || []).map((input) => input.name),
                            }
                        })
                    } else {
                        // Map the variants to an array of promises
                        const promises = variants.map((variant) =>
                            getAllVariantParameters(appId, variant).then((data) => ({
                                variantName: variant.variantName,
                                inputs:
                                    data?.inputs.map((inputParam: Parameter) => inputParam.name) ||
                                    [],
                            })),
                        )

                        // Wait for all promises to complete and collect results
                        results = await Promise.all(promises)
                    }

                    // Reduce the results into the desired newVariantsInputs object structure
                    const newVariantsInputs: Record<string, string[]> = results.reduce(
                        (acc: GenericObject, result) => {
                            acc[result.variantName] = result.inputs
                            return acc
                        },
                        {},
                    )

                    setVariantsInputs(newVariantsInputs)
                } catch (e: any) {
                    setIsError("Failed to fetch some variants parameters. Error: " + e?.message)
                }
            }

            fetchAndSetSchema()
        }
    }, [appId, variants])

    useEffect(() => {
        if (!isTestsetsLoadingError && testsets) {
            setTestsetsList((prev) => {
                if (isEqual(prev, testsets)) {
                    return prev
                }

                return testsets
            })
        }
    }, [testsets, isTestsetsLoadingError])

    const onTestsetSelect = (selectedTestsetIndexInTestsetsList: number) => {
        setSelectedTestset(testsetsList[selectedTestsetIndexInTestsetsList])
    }

    const getTestsetDropdownMenu = (): MenuProps => {
        const items: MenuProps["items"] = testsetsList.map((testset, index) => {
            return {
                label: (
                    <>
                        <div>{testset.name}</div>
                    </>
                ),
                key: `${testset.name}-${testset._id}`,
            }
        })

        const menuProps: MenuProps = {
            items,
            onClick: ({key}) => {
                const index = items.findIndex((item) => item?.key === key)
                onTestsetSelect(index)
            },
        }

        return menuProps
    }

    const handleAppVariantsMenuClick =
        (dropdownIndex: number) =>
        ({key}: {key: string}) => {
            const data = {
                variants: [
                    selectedVariants[dropdownIndex]?.variantName,
                    selectedVariants[dropdownIndex]?.variantName,
                ],
            }

            data.variants[dropdownIndex] = key
            const _selectedVariant = variants.find((variant) => variant.variantName === key)
            const selectedVariant = (_selectedVariant?.revisions || []).sort(
                (a, b) => b.updatedAtTimestamp - a.updatedAtTimestamp,
            )[0]
            if (!selectedVariant) {
                console.error("Error: No variant found")
            }

            setSelectedVariants((prevState) => {
                const newState = [...prevState]
                newState[dropdownIndex] = selectedVariant
                return newState
            })
        }

    const getVariantsDropdownMenu = (index: number): MenuProps => {
        const selectedVariantsNames = selectedVariants.map(
            (revision) => revision.__parentVariant?.variantName,
        )

        const items = variants.reduce((filteredVariants, variant, idx) => {
            const label = variant.variantName

            if (!selectedVariantsNames.includes(label)) {
                const isLatest = variant.revisions.some((revision) => revision.isLatestRevision)
                variant.isLatestRevision = isLatest
                filteredVariants.push({
                    label: (
                        <>
                            <div className="flex items-center justify-between">
                                <VariantDetailsWithStatus
                                    variantName={variant.variantName || variant.name}
                                    revision={variant.revision}
                                    variant={variant}
                                />
                                <span className={classes.dropdownItemLabels}>
                                    #
                                    {
                                        (
                                            variant.variantId ||
                                            variant.id ||
                                            variant.variant_id
                                        ).split("-")[0]
                                    }
                                </span>
                            </div>
                        </>
                    ),
                    key: label,
                })
            }

            return filteredVariants
        }, [])

        const menuProps: MenuProps = {
            items,
            onClick: handleAppVariantsMenuClick(index),
        }

        return menuProps
    }

    const onStartEvaluation = async () => {
        const selectedVariant = selectedVariants[0]
        // 1. We check all data is provided
        if (selectedTestset === undefined || selectedTestset.name === "Select a Test set") {
            message.error("Please select a Testset")
            return
        } else if (selectedVariant?.variantName === "Select a variant") {
            message.error("Please select a variant")
            return
        } else if (
            evaluationType === EvaluationType.human_a_b_testing &&
            selectedVariants[1]?.variantName === "Select a variant"
        ) {
            message.error("Please select a second variant")
            return
        }

        // 2. We create a new app evaluation
        const evaluationTableId = await createNewEvaluation({
            variant_ids: selectedVariants.map((variant) => variant.variantId || variant.id),
            appId,
            inputs: variantsInputs[selectedVariant.variantName],
            evaluationType: EvaluationType[evaluationType as keyof typeof EvaluationType],
            evaluationTypeSettings: {},
            llmAppPromptTemplate: "",
            selectedCustomEvaluationID: _selectedCustomEvaluationID,
            testsetId: selectedTestset._id!,
        }).catch((err) => {
            if (err.message !== PERMISSION_ERR_MSG) {
                setError({
                    message: getErrorMessage(err),
                    btnText: "Go to Test sets",
                    endpoint: `/testsets`,
                })
            }
        })

        if (!evaluationTableId) {
            return
        }

        // 3 We set the variants
        // setVariants(selectedVariants)

        if (evaluationType === EvaluationType.human_a_b_testing) {
            router.push(`/apps/${appId}/evaluations/human_a_b_testing/${evaluationTableId}`)
        } else if (evaluationType === EvaluationType.single_model_test) {
            router.push(`/apps/${appId}/evaluations/single_model_test/${evaluationTableId}`)
        }
    }

    return (
        <>
            <Modal
                open={isEvalModalOpen}
                onCancel={() => {
                    setIsEvalModalOpen(false)

                    setSelectedTestset({name: "Select a Test set"})
                    setSelectedVariants(new Array(1).fill({variantName: "Select a variant"}))
                }}
                title="New Evaluation"
                footer={null}
            >
                <Spin spinning={areAppVariantsLoading}>
                    {typeof isError === "string" ? (
                        <div style={{margin: "20px 0"}}>{isError}</div>
                    ) : (
                        <div style={{display: "flex", flexDirection: "column", gap: 10}}>
                            <div>
                                <p>Which testset you want to use?</p>
                                <Dropdown menu={getTestsetDropdownMenu()}>
                                    <Button className={classes.dropdownBtn}>
                                        <div className={classes.dropdownStyles}>
                                            {selectedTestset.name}
                                            <CaretDown size={16} />
                                        </div>
                                    </Button>
                                </Dropdown>
                            </div>

                            <div>
                                <p>Which variants would you like to evaluate</p>
                                {Array.from({
                                    length: evaluationType === "human_a_b_testing" ? 2 : 1,
                                }).map((_, index) => (
                                    <Dropdown key={index} menu={getVariantsDropdownMenu(index)}>
                                        <Button
                                            className={classes.variantDropdown}
                                            style={{marginTop: index === 1 ? 8 : 0}}
                                        >
                                            <div className={classes.dropdownStyles}>
                                                {selectedVariants[index]?.variantName ||
                                                    "Select a variant"}
                                                <CaretDown size={16} />
                                            </div>
                                        </Button>
                                    </Dropdown>
                                ))}
                            </div>

                            <Row justify="end" gutter={8} style={{marginTop: "1.5rem"}}>
                                <Button
                                    style={{marginRight: "auto"}}
                                    key="cancel"
                                    onClick={() => setIsEvalModalOpen(false)}
                                >
                                    Cancel
                                </Button>
                                {evaluationType === EvaluationType.human_a_b_testing &&
                                    isDemo() && (
                                        <Col>
                                            <Button
                                                disabled={
                                                    !(
                                                        selectedVariants[0].variantId &&
                                                        selectedVariants[0].variantId &&
                                                        selectedTestset._id
                                                    )
                                                }
                                                onClick={() => setShareModalOpen(true)}
                                            >
                                                Invite Collaborators
                                            </Button>
                                        </Col>
                                    )}
                                <Col>
                                    <Button
                                        onClick={onStartEvaluation}
                                        type="primary"
                                        icon={<Play size={14} />}
                                        className="flex items-center"
                                    >
                                        Start
                                    </Button>
                                </Col>
                            </Row>
                        </div>
                    )}
                </Spin>
            </Modal>

            <EvaluationErrorModal
                isModalOpen={!!error.message}
                onClose={() => setError({message: "", btnText: "", endpoint: ""})}
                handleNavigate={() => router.push(error.endpoint)}
                message={error.message}
                btnText={error.btnText}
            />

            <ShareEvaluationModal
                open={shareModalOpen}
                onCancel={() => setShareModalOpen(false)}
                destroyOnClose
                variantIds={selectedVariants.map((v) => v.variantId)}
                testsetId={selectedTestset._id}
                evaluationType={EvaluationType.human_a_b_testing}
            />
        </>
    )
}

export default HumanEvaluationModal
