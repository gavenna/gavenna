<img src="assets/hero.svg" alt="gavenna — 把直播间做成可编程的游乐场" width="100%" />

我把直播间做成可编程的游乐场：弹幕和礼物接进状态机，LLM 接进话术引擎，画面交给 Godot。

## livegame · 直播间互动游戏

一个能真的开播的互动游戏，不是演示。`直播弹幕 → 兵种与阵营 → 战局结算 → 主播话术播报 → OBS 画面`，整条链路在一个仓库里。画面侧 Godot，链路侧 Node，抖音弹幕接入，打包成单 exe 一键启动。

它把不确定性也写进了仓库——`HANDOVER.md` 分三类记录：

| 分类 | 说明 |
|---|---|
| 已修复 | 逐条带根因，例如「模板插值 `val !== undefined` 不防 null → 改 `val != null` + 残留占位符兜底清除」 |
| assumed（未逐条验证） | 「LLM 话术代码完整但 `LLM_ENABLED=false`，缺 API Key」「真实弹幕/礼物链路未经实际观众验证」 |
| failed_approaches | 走不通的路也留着，避免下一轮重新踩 |

配套还有 `PROGRESS.md`，以及按游戏时间线排的话术验收清单——上线前照着听一场，7 条"不通过信号"里任意一条就是系统有问题。

`godot/`　`server/`　`frontend/`　`toolbox/`　`setup.iss`

[仓库](https://github.com/gavenna/livegame) · [交接文档](https://github.com/gavenna/livegame/blob/main/HANDOVER.md) · [使用指南](https://github.com/gavenna/livegame/blob/main/docs/使用指南.md)

## 我在这个项目里坚持的三件事

1. **把"没验证"写出来，而不是装作验证过。** 交接文档里 `assumed` 是独立一节，和"已修复"分开。
2. **I/O 注入，让核心逻辑是纯函数。** 能单测的东西不该被文件系统和网络绑住。
3. **失败的路也留着。** `failed_approaches` 记下每条走不通的方案和原因，避免下一轮重新踩。

## 联系

[博客](https://gavenna.github.io)
