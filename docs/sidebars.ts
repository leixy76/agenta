// @ts-check
import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const CATEGORY_UTILITIES: any = {
  type: "category",
  collapsed: false,
  collapsible: false,
  className: "sidebar-section-title",
};

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      label: "Getting Started",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "getting_started" }],
    },
    {
      label: "Prompt Management",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "prompt_management" }],
    },
    {
      label: "Evaluation",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "evaluation" }],
    },
    {
      label: "Observability",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "observability" }],
    },
    {
      label: "Self-host",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "self-host" }],
    },
    {
      label: "Misc",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "misc" }],
    },
  ],
  guidesSidebar: [
    {
      label: "Introduction",
      ...CATEGORY_UTILITIES,
      items: [{ type: "doc", id: "guides/how_does_agenta_work" }],
    },
    {
      label: "Tutorials",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "guides/tutorials" }],
    },
    {
      label: "Cookbooks",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "guides/cookbooks" }],
    },
  ],
  refrenceSidebar: [
    {
      label: "Python SDK",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "reference/sdk" }],
    },
    {
      label: "Command Line",
      ...CATEGORY_UTILITIES,
      items: [{ type: "autogenerated", dirName: "reference/cli" }],
    },
    {
      label: "API Reference",
      ...CATEGORY_UTILITIES,
      link: {
        type: "generated-index",
        title: "APIs",
        description: "This is a sample server Agenta.io server.",
        slug: "/reference/api/category",
      },
      // @ts-ignore
      items: require("./docs/reference/api/sidebar.js"),
    },
  ],
};

export default sidebars;
