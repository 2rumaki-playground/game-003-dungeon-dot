# 開発ガイド

## 前提条件

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [go-task](https://taskfile.dev/)
- （オプション）[mise](https://mise.jdx.dev/) -- ツールバージョン管理

## セットアップ

```bash
# mise でツールをインストール（推奨）
mise install

# 依存関係のインストール
task install
```

## よく使うコマンド

| コマンド | 説明 |
|---------|------|
| `task dev` | ゲーム起動 |
| `task check` | 全チェック一括実行 |
| `task test` | テスト実行 |
| `task fix` | lint + format 自動修正 |
| `task --list` | 全タスク一覧 |

## アーキテクチャ

### レイヤー構造

```
presentation → infrastructure → domain
```

- **domain**: 純粋なゲームロジック。`pyxel` や `wandb` をimportしない
- **presentation**: Pyxel描画・入力処理。`domain` と `infrastructure` に依存
- **infrastructure**: 外部サービス。`domain` にのみ依存
- **config**: Hydra設定スキーマ

この依存方向は `import-linter` で自動検証される（`task deps:check`）。

### Hydra設定

`conf/` 配下のYAMLファイルで設定を管理。コマンドラインからオーバーライド可能：

```bash
task dev             # デフォルト設定
task dev:debug       # game=debug で起動
```

## コミット規約

`.github/git-commit-instructions.md` 参照。Conventional Commits形式、日本語、50文字以内。
