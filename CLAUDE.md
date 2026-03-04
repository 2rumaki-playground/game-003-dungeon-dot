# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

ドット絵のランダム生成ダンジョン攻略ゲーム。Pyxel エンジンで描画、Python で実装。

## 仕様ドキュメント

すべての仕様は `docs/spec/` 配下で管理。一覧は `docs/spec/readme.md` を参照。

特に重要なファイル：
- `constants.md` -- 数値パラメータの**正典（Single Source of Truth）**

## 基本方針

### 後方互換性は不要
- リリース前の開発段階であり、後方互換性を一切考慮しない
- deprecated マーク、互換shim、旧名称の再エクスポート等は禁止
- インターフェース変更時は旧APIを残さず、使用箇所をすべて書き換える

### 最小差分
- 必要な範囲だけ変更。関係ない整形・言い回し変更はしない

### 根本原因の修正
- 暫定対応・ハック修正は禁止。必ず根本原因を修正する

### 単一の拠り所
- 同じ数値やルールを複数箇所に重複して書かない
- 数値は必ず `constants.py`（`docs/spec/constants.md` に対応）を参照

### 仕様の穴は可視化
- 曖昧点は勝手に決めずにIssue化

### アーキテクチャの制約
- **domainレイヤーは `pyxel` をimportしない**（純粋なゲームロジック）
- import-linter で以下の依存方向を強制:
  - `domain` → 外部依存なし（pyxel, wandb 禁止）
  - `infrastructure` → `domain` のみ
  - `presentation` → `domain`, `infrastructure`
- この制約により、domain層は単体テストで高速にテスト可能

## 作業の進め方

### 計画ファースト
- 3ステップ以上の作業や設計判断を伴う変更は、必ず計画を立ててから実装する

### 完了条件
以下を満たさない限り、タスクを完了としない：
- `task test` でユニットテストが全通過している
- `task typecheck` で型チェックが通っている
- `task deps:check` で依存チェックが通っている

### バグ修正
- バグ報告を受けたら、追加の指示を求めず調査・修正を進める

## コミットメッセージ

`.github/git-commit-instructions.md` に従う。Conventional Commits形式、**日本語**、50文字以内。

## 開発コマンド

```bash
task install       # 依存関係のインストール
task dev           # ゲーム起動
task dev:debug     # デバッグモードでゲーム起動
task lint          # Ruffによるリント
task lint:fix      # リント自動修正
task format        # Ruffによるフォーマット
task format:check  # フォーマットチェック
task typecheck     # tyによる型チェック
task deps:check    # import-linterによる依存チェック
task test          # ユニットテスト実行
task test:cov      # カバレッジ付きテスト
task test:fast     # slowマーク以外のテスト
task bench         # ベンチマーク実行
task check         # 全チェック一括実行（CI相当）
task fix           # lint + format 自動修正
task tox           # tox全環境テスト
task clean         # アーティファクト削除
```

## 技術スタック

Python / Pyxel / Hydra / wandb / uv / Ruff / ty / pytest / import-linter / tox / go-task

## ディレクトリ構造

```
src/dungeon_dot/
├── __main__.py        # エントリーポイント
├── app.py             # Pyxel Appクラス
├── constants.py       # 定数（docs/spec/constants.md に対応）
├── domain/            # ゲームロジック（Pyxelに依存しない）
├── presentation/      # Pyxel描画
├── infrastructure/    # 外部サービス（wandb, ストレージ）
└── config/            # Hydra設定スキーマ
conf/                  # Hydra YAML設定ファイル
tests/                 # テスト（src構造をミラー）
```

## 言語

すべての出力は**日本語**で行う（PR概要、Issue、コミットメッセージ含む）。
