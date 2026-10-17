# PrintCraft skills

Prerelease **0.1.0-dev.6**, pinned printcraft-cli 0.2.1 for macOS arm64 / Python 3.11+.
Six independently installable skills provide runtime diagnostics, PDF inspection/page edits, single-session plans, uncertain-outcome reconciliation and digest-bound artifact verification.

Execution and verification use independent versioned protocols. A zero exit is not delivery acceptance. Native sample evidence is separate from host/model, OCR, cross-plugin and release gates. Explicit optional Tesseract Chinese OCR is validated on macOS arm64; pinned native OCR remains English-only. Five native platforms have separate direct-runtime evidence; the skill installer supports macOS arm64. Mobile-device delivery remains unverified. See project-status.json for the current publication receipt.

See [中文使用说明](README.zh-CN.md), [implementation evidence](docs/verification/implementation-2026-10-08.md), and [OpenSpec tasks](openspec/changes/harden-printcraft-skill-execution/tasks.md).

Install a single skill from the immutable prerelease:

```bash
npx skills add https://github.com/full-aigc-skills/printcraft-skills/tree/v0.1.0-dev.6/skills/printcraft-use
```

[Release](https://github.com/full-aigc-skills/printcraft-skills/releases/tag/v0.1.0-dev.6). This is a development prerelease, not full platform or production acceptance.

## 场景技能开发候选

已增加 6 个领域场景技能及 1 个内嵌编辑器入口。详见 [场景目录](docs/scene-skills.md)。本地未发布候选，不代表全部场景的创作质量已验收。

## main交付检查候选

新增[main工具指导](skills/printcraft-pdf-preflight/references/main-workflows.md)：所选页字数、未标记内容定位及7个新增工具/16处契约变化。新增统计/定向检查已通过Windows main专项39008588714；不等于完整无障碍认证，不改变既有中文表单外观限制。

## PDF交付场景技能

以下独立技能自带完整步骤、当前原生工具schema、来源固定提交及CLI脚本编译器；不会改动冻结的六个基础技能。命令目录和技术回归不代表所有真实PDF或宿主同步已验收。

| 技能 | 任务与交付 |
| --- | --- |
| `printcraft-report-bookmarks` | 按确认章节页建立层级书签，保留原页内容 |
| `printcraft-review-watermark` | 只给选定审阅页加水印，检查非目标页不变 |
| `printcraft-invoice-split` | 按确认的单据起始页拆包，逐页核对无丢失与跨单据 |
| `printcraft-section-pagination` | 前言与正文分别添加可见页脚编号，区分PDF物理页和阅读编号 |
| `printcraft-linked-agenda` | 议程与附录双向内部跳转，核对热点和目标页 |
| `printcraft-revision-compare` | 对照新旧PDF生成文字差异报告，保留两个原件 |

本批作为开发候选集成，实际安装版本以市场条目和对应发布标签为准。当前后端工具缺失时如实报告，不将示例ID、页号和坐标直接套用真实文件。
