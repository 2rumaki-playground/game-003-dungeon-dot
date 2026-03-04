# Copilot 指示

## 言語

すべての出力（コードコメント、PR、Issue、コミットメッセージ）は**日本語**で記述すること。

## アーキテクチャ

- `domain/` レイヤーは `pyxel` や `wandb` をimportしない（純粋なゲームロジック）
- 依存方向: `presentation` → `infrastructure` → `domain`
- 数値定数は `constants.py` に集約（`docs/spec/constants.md` が正典）

## コーディング規約

- Ruff準拠（`pyproject.toml` `[tool.ruff]` 参照）
- ダブルクォート、line-length=99
- 型ヒント必須

## 後方互換性は不要

リリース前の開発段階。deprecated マーク、互換shim、旧名称の再エクスポートは禁止。
