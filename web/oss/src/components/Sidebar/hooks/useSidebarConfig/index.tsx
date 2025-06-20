import {AppstoreOutlined, DatabaseOutlined, GithubFilled} from "@ant-design/icons"
import {
    ChartDonut,
    ChartLineUp,
    Desktop,
    PaperPlane,
    Phone,
    Question,
    Scroll,
    SlackLogo,
    Gear,
    TreeView,
    Lightning,
    Rocket,
    CloudArrowUp,
    ChatCircle,
} from "@phosphor-icons/react"

import {useAppsData} from "@/oss/contexts/app.context"
import {useOrgData} from "@/oss/contexts/org.context"
import {useAppId} from "@/oss/hooks/useAppId"
import {useCrispChat} from "@/oss/hooks/useCrispChat"
import {useSession} from "@/oss/hooks/useSession"
import {isDemo} from "@/oss/lib/helpers/utils"

import {SidebarConfig} from "../../types"

export const useSidebarConfig = () => {
    const appId = useAppId()
    const {doesSessionExist} = useSession()
    const {currentApp, recentlyVisitedAppId} = useAppsData()
    const {selectedOrg} = useOrgData()
    const {toggle, isVisible, isCrispEnabled} = useCrispChat()

    const sidebarConfig: SidebarConfig[] = [
        {
            key: "app-management-link",
            title: "App Management",
            tooltip: "Create new applications or switch between your existing projects.",
            link: "/apps",
            icon: <AppstoreOutlined size={16} />,
        },
        {
            key: "app-testsets-link",
            title: "Test Sets",
            tooltip: "Create and manage testsets for evaluation purposes.",
            link: `/testsets`,
            icon: <DatabaseOutlined size={16} />,
        },
        {
            key: "app-observability-link",
            title: "Observability",
            link: `/observability`,
            icon: <ChartLineUp size={16} />,
            divider: true,
        },
        {
            key: `${currentApp?.app_name || ""}_key`,
            title: currentApp?.app_name || "",
            icon: <></>,
            header: true,
        },
        {
            key: "overview-link",
            title: "Overview",
            link: `/apps/${appId || recentlyVisitedAppId}/overview`,
            icon: <Desktop size={16} />,
            isHidden: !appId && !recentlyVisitedAppId,
        },
        {
            key: "app-playground-link",
            title: "Playground",
            tooltip:
                "Experiment with real data and optimize your parameters including prompts, methods, and configuration settings.",
            link: `/apps/${appId || recentlyVisitedAppId}/playground`,
            icon: <Rocket size={16} />,
            isHidden: !appId && !recentlyVisitedAppId,
        },
        {
            key: "app-variants-link",
            title: "Registry",
            link: `/apps/${appId || recentlyVisitedAppId}/variants`,
            isHidden: !appId && !recentlyVisitedAppId,
            icon: <Lightning size={16} />,
        },
        {
            key: "app-evaluations-link",
            title: "Evaluations",
            link: `/apps/${appId || recentlyVisitedAppId}/evaluations`,
            isHidden: (!appId && !recentlyVisitedAppId) || !isDemo(),
            icon: <ChartDonut size={16} />,
        },
        {
            key: "app-traces-link",
            title: "Traces",
            icon: <TreeView size={16} />,
            isHidden: !appId && !recentlyVisitedAppId,
            link: `/apps/${appId || recentlyVisitedAppId}/traces`,
        },
        {
            key: "app-deployments-link",
            title: "Deployments",
            link: `/apps/${appId || recentlyVisitedAppId}/deployments`,
            isHidden: !appId && !recentlyVisitedAppId,
            icon: <CloudArrowUp size={16} />,
        },
        {
            key: "invite-teammate-link",
            title: "Invite Teammate",
            link: "/settings?tab=workspace&inviteModal=open",
            icon: <PaperPlane size={16} />,
            isBottom: true,
            isHidden: !doesSessionExist || !selectedOrg,
        },
        {
            key: "settings-link",
            title: "Settings",
            link: "/settings",
            icon: <Gear size={16} />,
            isBottom: true,
            isHidden: true,
        },
        {
            key: "support-chat-link",
            title: `Live Chat Support: ${isVisible ? "On" : "Off"}`,
            icon: <ChatCircle size={16} />,
            isBottom: true,
            isHidden: !isDemo() || !isCrispEnabled,
            onClick: (e) => {
                e.preventDefault()
                toggle()
            },
        },
        {
            key: "help-docs-link",
            title: "Help & Docs",
            icon: <Question size={16} />,
            isBottom: true,
            submenu: [
                {
                    key: "docs",
                    title: "Documentation",
                    link: "https://docs.agenta.ai/",
                    icon: <Scroll size={16} />,
                },
                {
                    key: "github-support",
                    title: "GitHub Support",
                    link: "https://github.com/Agenta-AI/agenta/issues",
                    icon: <GithubFilled size={16} />,
                },
                {
                    key: "slack-connect",
                    title: "Slack Support",
                    link: "https://join.slack.com/t/agenta-hq/shared_invite/zt-37pnbp5s6-mbBrPL863d_oLB61GSNFjw",
                    icon: <SlackLogo size={16} />,
                },
                {
                    key: "book-call",
                    title: "Book a call",
                    link: "https://cal.com/mahmoud-mabrouk-ogzgey/demo",
                    icon: <Phone size={16} />,
                },
            ],
        },
    ]

    return sidebarConfig
}
