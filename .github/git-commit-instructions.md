# コミットメッセージ規約

## 形式

Conventional Commits 形式に従う。

```
<type>: <subject>
```

## type

- `feat`: 新機能
- `fix`: バグ修正
- `refactor`: リファクタリング
- `docs`: ドキュメント変更
- `test`: テスト追加・修正
- `chore`: ビルド・CI・設定変更
- `perf`: パフォーマンス改善
- `style`: フォーマット変更（動作に影響なし）

## ルール

- **日本語**で記述
- subject は **50文字以内**
- 末尾にピリオドをつけない
- 命令形で書く（「追加する」ではなく「追加」）

## 例

```
feat: ダンジョン自動生成を追加
fix: プレイヤーのHP計算が負数になる問題を修正
refactor: 戦闘処理をdomain層に分離
test: ダンジョン生成の再現性テストを追加
chore: CI にimport-linterチェックを追加
```
