# game-003-dungeon-dot

ドット絵のランダム生成ダンジョン攻略ゲーム

## 技術スタック

| カテゴリ | ツール |
|---------|--------|
| 言語 | Python 3.12+ |
| ゲームエンジン | Pyxel |
| パッケージ管理 | uv |
| リンター/フォーマッター | Ruff |
| 型チェック | ty |
| テスト | pytest / tox |
| 依存チェック | import-linter |
| タスクランナー | Taskfile (go-task) |
| 設定管理 | Hydra |
| 実験トラッキング | wandb |

## セットアップ

```bash
# ツールのインストール（mise使用の場合）
mise install

# 依存関係のインストール
task install

# ゲーム起動
task dev
```

## 開発

```bash
task check    # 全チェック一括実行（format, lint, typecheck, deps, test）
task fix      # lint + format 自動修正
task test     # テスト実行
task --list   # 全タスク一覧
```

## アーキテクチャ

```
presentation → infrastructure → domain
```

- **domain**: 純粋なゲームロジック（Pyxel非依存、高速テスト可能）
- **presentation**: Pyxel描画・入力処理
- **infrastructure**: 外部サービス（wandb, セーブ/ロード）
- **config**: Hydra設定スキーマ
