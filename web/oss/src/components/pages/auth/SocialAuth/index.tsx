import {GithubOutlined, GoogleOutlined} from "@ant-design/icons"
import {Button, Divider} from "antd"
import {useRouter} from "next/router"
import {getAuthorisationURLWithQueryParamsAndSetState} from "supertokens-auth-react/recipe/thirdparty"

import {getEnv} from "@/oss/lib/helpers/dynamicEnv"

import {SocialAuthProps} from "../assets/types"

const SocialAuth = ({authErrorMsg, isLoading, setIsLoading, disabled}: SocialAuthProps) => {
    const router = useRouter()

    const googleSignInClicked = async () => {
        try {
            setIsLoading(true)

            const authUrl = await getAuthorisationURLWithQueryParamsAndSetState({
                thirdPartyId: "google",
                frontendRedirectURI: `${
                    getEnv("NEXT_PUBLIC_AGENTA_WEB_URL") || getEnv("NEXT_PUBLIC_AGENTA_API_URL")
                }/auth/callback/google`,
            })

            router.push(authUrl)
        } catch (err) {
            authErrorMsg(err)
        } finally {
            setIsLoading(false)
        }
    }

    const githubSignInClicked = async () => {
        try {
            setIsLoading(true)

            const authUrl = await getAuthorisationURLWithQueryParamsAndSetState({
                thirdPartyId: "github",
                frontendRedirectURI: `${
                    getEnv("NEXT_PUBLIC_AGENTA_WEB_URL") || getEnv("NEXT_PUBLIC_AGENTA_API_URL")
                }/auth/callback/github`,
            })

            router.push(authUrl)
        } catch (err) {
            authErrorMsg(err)
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <>
            <div className="flex flex-col gap-2">
                <Button
                    icon={<GoogleOutlined />}
                    size="large"
                    className="w-full"
                    onClick={googleSignInClicked}
                    loading={isLoading}
                    disabled={disabled}
                >
                    Continue with Google
                </Button>

                <Button
                    icon={<GithubOutlined />}
                    size="large"
                    className="w-full"
                    onClick={githubSignInClicked}
                    loading={isLoading}
                    disabled={disabled}
                >
                    Continue with Github
                </Button>
            </div>

            <Divider className="!m-0">or</Divider>
        </>
    )
}

export default SocialAuth
