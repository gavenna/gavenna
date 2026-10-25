<img src="assets/hero.svg" alt="gavenna — 把直播间做成可编程的游乐场" width="100%" />

我把直播间做成可编程的游乐场：弹幕和礼物接进状态机，LLM 接进话术引擎，画面交给 Godot。顺带给 AI agent 的工具链写零依赖插件。

<!-- STATS-START -->
🛠 12 个公开仓库 · 最近推送 2026-09-30
<!-- STATS-END -->

## 最近在做：直播间互动系统

一个能真的开播的互动游戏，而不是一个演示。

`直播弹幕 → 兵种与阵营 → 战局结算 → 主播话术播报 → OBS 画面`，整条链路在一个仓库里。画面侧是 Godot 客户端，链路侧是 Node 服务端。

它把不确定性也写进了仓库——HANDOVER.md 里分三类记录：

| 分类 | 说明 |
|---|---|
| 已修复 | 逐条带根因，例如「模板插值 `val !== undefined` 不防 null → 改 `val != null` + 残留占位符兜底清除」 |
| assumed（未逐条验证） | 「LLM 话术代码完整但 `LLM_ENABLED=false`，缺 API Key」「真实弹幕/礼物链路未经实际观众验证」 |
| failed_approaches | 走不通的路也留着，避免下一轮重新踩 |

配套还有 PROGRESS.md 与按游戏时间线排的话术验收清单（主播可以对着听）。

[打开 livegame →](https://github.com/gavenna/livegame)

## 从这里开始

### livegame · 直播间互动游戏

Godot 客户端 + Node 服务端 + 弹幕/礼物链路 + LLM 话术引擎 + OBS 挂图。跨平台启动脚本（bat / ps1 / sh）与安装包配置齐全。

`godot/`　`server/`　`frontend/`　`toolbox/`　`setup.iss`

[仓库](https://github.com/gavenna/livegame) · [交接文档](https://github.com/gavenna/livegame/blob/main/HANDOVER.md)

### dsh-health-check · 给 dsh 做体检的零依赖插件

四个 checker 覆盖装完之后的常见坑，I/O 全部注入，checker 是纯函数，vitest + 全 stub。零运行时依赖。

| Checker | 查什么 | 结果 |
|---|---|---|
| `version` | dsh manifest 名字 + 版本 | readable / missing |
| `bin-links` | `.bin/dsh` 链接是否齐全 | all present / 列出缺失项 |
| `config-dump` | `--dump-config` 组合结果 | markers + entries / empty |
| `port` | 目标端口占用 | free / listening |

`config-dump` 走的是 boot-free、离线、只读的渲染——不调 LLM、不碰凭据。

[打开仓库 →](https://github.com/gavenna/dsh-health-check)

## 给 AI Agent 配上工具

### dsh-aqua-glass · dsh 的 Aqua 玻璃拟态适配

上游停更在 rc.5 前端 API，dsh 0.1.3-alpha.1 的 client 架构拆成了 store 引擎 + modules 模块系统。仓库里有一张**逐行的 API 漂移适配表**：

| 上游（rc.5） | alpha.1 现状 | 适配动作 |
|---|---|---|
| `dsh-client-runtime` | 拆为 `dsh-client-store` + `dsh-client-modules` | import 改指向 store |
| `ctx.slots` 由 settings 系带出 | 由 `dsh-client-ui-renderer/client` 提供 | 补 type-only import |
| `settings.plugin.item` 槽 | 改为 keyed 架构 | 主开关降级到 `settings.general.item`（order 12） |
| `queryPermission` / `requestPermission` | 已从 DOM lib 移除 | 改用 `getFile` 探测读授权 |
| `noUncheckedIndexedAccess` 关闭 | 构建链默认开启 | 局部 tsconfig 豁免，不动动画数学代码 |

所有层都是 effect，一键关闭即还原原生 UI。上游版权保留，同以 AGPL-3.0 发布。

[打开仓库 →](https://github.com/gavenna/dsh-aqua-glass) · [上游项目](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin)

### live_tool · 弹幕战斗工具链

`danmaku/`　`battle/`　`mods/`　`relay.js`　`server/` —— mod 可插拔的弹幕战斗服务，带独立测试入口。

[打开仓库 →](https://github.com/gavenna/live_tool)

## 站点

- **gavenna.github.io** — Hugo 博客，长文与技术笔记
- **resume-site** — 双语简历站：`build.py` 把 Markdown + YAML frontmatter 编成 HTML，零 Node 依赖，Netlify 自动部署，暗色模式 + Intersection Observer 滚动揭示

## 我在每个仓库里都会做的三件事

1. **把"没验证"写出来，而不是装作验证过。** 交接文档里 `assumed` 是独立一节，和"已修复"分开。
2. **I/O 注入，让核心逻辑是纯函数。** 能单测的东西不该被文件系统和端口绑住。
3. **零依赖优先。** 能用标准库就不加包——`dsh-health-check` 零运行时依赖，`resume-site` 零 Node 依赖。

## 联系

[博客](https://gavenna.github.io) · [全部仓库](https://github.com/gavenna?tab=repositories)
