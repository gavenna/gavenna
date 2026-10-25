<img src="assets/hero.svg" alt="gavenna — 把直播间做成可编程的游乐场" width="100%" />

我把直播间做成可编程的游乐场：弹幕和礼物接进状态机，LLM 接进话术引擎，画面交给游戏与桌宠。

## live-waifu · 虚拟主播直播互动套件

真正在跑的那一套。三个独立项目通过 WebSocket 协作，一键拉起，已在抖音直播跑通完整闭环并产生实际收入。

| 组件 | 是什么 |
|---|---|
| `danmaku-relay` | B站 / 抖音弹幕中继，可打包成独立 exe。`:8766` WS 广播、`:8767` 控制面板 |
| `war-danmaku` | 弹幕阵营对抗游戏，Node + Canvas。`:8765` 游戏通信、`:3000` OBS 画面源 |
| `waifu-agent` | Live2D 桌宠 + AI Agent，Tauri 2 / Rust / React。`:9191` 接收事件做播报 |

`start-all.ps1` 一键拉起全部，`-Stop` 释放端口。

现在实际跑的不是自研游戏——`danmaku-relay/battle` 直接驱动真实 Rusted Warfare，桌宠由中继经 `:9191` 播报战况和观众对话。这个改动把「弹幕改游戏」从写一个游戏变成了接一个游戏。

[仓库](https://github.com/gavenna/live-waifu) · [交接文档](https://github.com/gavenna/live-waifu/blob/main/HANDOVER.md) · [项目工作流](https://github.com/gavenna/live-waifu/blob/main/docs/项目工作流.md) · [直播指令手册](https://github.com/gavenna/live-waifu/blob/main/docs/直播指令手册.md)

## livegame · 自研弹幕游戏内核

`war-danmaku` 的独立仓库版：`直播弹幕 → 兵种与阵营 → 战局结算 → 主播话术播报 → OBS 画面`，整条链路在一个仓库里。画面侧 Godot，链路侧 Node，抖音弹幕接入，打包成单 exe。

它把不确定性也写进了仓库——`HANDOVER.md` 分三类记录：

| 分类 | 说明 |
|---|---|
| 已修复 | 逐条带根因，例如「模板插值 `val !== undefined` 不防 null → 改 `val != null` + 残留占位符兜底清除」 |
| assumed（未逐条验证） | 「LLM 话术代码完整但 `LLM_ENABLED=false`，缺 API Key」「真实弹幕/礼物链路未经实际观众验证」 |
| failed_approaches | 走不通的路也留着，避免下一轮重新踩 |

`godot/`　`server/`　`frontend/`　`toolbox/`　`setup.iss`

[仓库](https://github.com/gavenna/livegame) · [交接文档](https://github.com/gavenna/livegame/blob/main/HANDOVER.md)

## 我在这个项目里坚持的三件事

1. **把"没验证"写出来，而不是装作验证过。** 交接文档里 `assumed` 是独立一节，和"已修复"分开。
2. **I/O 注入，让核心逻辑是纯函数。** 能单测的东西不该被文件系统和网络绑住。
3. **失败的路也留着。** `failed_approaches` 记下每条走不通的方案和原因，避免下一轮重新踩。

## 联系

[博客](https://gavenna.github.io)
