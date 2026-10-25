<img src="assets/hero.svg" alt="gavenna — 把直播间做成可编程的游乐场" width="100%" />

我把直播间做成可编程的游乐场：弹幕和礼物接进状态机，LLM 接进话术引擎，画面交给 Godot。然后把「话术」那一层单独抽出来，做成任何直播间都能装的东西。

<!-- STATS-START -->
🛠 12 个公开仓库 · 最近推送 2026-10-25
<!-- STATS-END -->

## 最近在做：把话术变成调度问题

直播话术机 **`live-script`** —— 主播不是不会说话，是不知道第 47 分钟该说什么。

写 100 句漂亮的话，不如定对 5 条规则：

| 规则 | 为什么 |
|---|---|
| 付费永不防抖 | 观众付费后 3 秒没被念到名字，这个行为就不会再发生 |
| 高光必须插队 | 情绪峰值只有 2 秒，延迟超过 2 秒就是复述 |
| 冲突必须聚合 | 3 次各掉 50 血只播一次"掉了 150"，观众要趋势不要流水账 |
| 模板给速度，LLM 给变化 | 高频事件秒出，依赖上下文的 30s 一次、超时 10s 降级 |
| 填充必须检测变化 | 数值变化 <10% 且人员/进度没变，就别开口 |

里面还有一张**可填的验收清单**——上线前照着听一场，7 条"不通过信号"中任意一条就是系统有问题。多数人给完话术就结束了，没有判据。

[打开 live-script →](https://github.com/gavenna/live-script-skill) · [直接读 SKILL.md](https://github.com/gavenna/live-script-skill/blob/main/SKILL.md)

## 从这里开始

### livegame · 直播间互动游戏

一个能真的开播的互动游戏，不是演示。`直播弹幕 → 兵种与阵营 → 战局结算 → 主播话术播报 → OBS 画面`，整条链路在一个仓库里。画面侧 Godot，链路侧 Node，B站弹幕接入，一键启动。

它把不确定性也写进了仓库——HANDOVER.md 分三类记录：

| 分类 | 说明 |
|---|---|
| 已修复 | 逐条带根因，例如「模板插值 `val !== undefined` 不防 null → 改 `val != null` + 残留占位符兜底清除」 |
| assumed（未逐条验证） | 「LLM 话术代码完整但 `LLM_ENABLED=false`，缺 API Key」「真实弹幕/礼物链路未经实际观众验证」 |
| failed_approaches | 走不通的路也留着，避免下一轮重新踩 |

配套还有 PROGRESS.md 与按游戏时间线排的话术验收清单。

`godot/`　`server/`　`frontend/`　`toolbox/`　`setup.iss`

[仓库](https://github.com/gavenna/livegame) · [交接文档](https://github.com/gavenna/livegame/blob/main/HANDOVER.md) · [使用指南](https://github.com/gavenna/livegame/blob/main/docs/使用指南.md)

### live_tool · 弹幕战斗工具链

`danmaku/`　`battle/`　`mods/`　`relay.js`　`server/` —— mod 可插拔的弹幕战斗服务，带独立测试入口。

弹幕接进来，battle 模块算，mods 让规则可换。同一套链路既能服务小游戏，也能当战斗逻辑的实验场。

[打开仓库 →](https://github.com/gavenna/live_tool)

## 给 AI Agent 装上

- **[live-script](https://github.com/gavenna/live-script-skill)** —— 直播话术调度：优先级 + 防抖 + 双路径 + 情绪曲线，自带验收清单。一行安装：
  `git clone https://github.com/gavenna/live-script-skill.git ~/.claude/skills/live-script`

## 站点

- **gavenna.github.io** — Hugo 博客，长文与技术笔记
- **resume-site** — 双语简历站：`build.py` 把 Markdown + YAML frontmatter 编成 HTML，零 Node 依赖，Netlify 自动部署，暗色模式 + Intersection Observer 滚动揭示

## 我在每个仓库里都会做的三件事

1. **把"没验证"写出来，而不是装作验证过。** 交接文档里 `assumed` 是独立一节，和"已修复"分开。
2. **I/O 注入，让核心逻辑是纯函数。** 能单测的东西不该被文件系统和网络绑住。
3. **零依赖优先。** 能用标准库就不加包——`live-script` 零依赖不联网，`resume-site` 的构建链零 Node 依赖。

## 联系

[博客](https://gavenna.github.io) · [全部仓库](https://github.com/gavenna?tab=repositories)
