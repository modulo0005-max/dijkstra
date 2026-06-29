const express = require('express');
const path = require('path');
const app = express();

// 포트 설정 (환경 변수 PORT가 없으면 8080 사용)
const port = process.env.PORT || 8080;

// 현재 폴더의 모든 정적 파일 제공
app.use(express.static(path.join(__dirname, '.')));

app.listen(port, () => {
  console.log(`서버가 포트 ${port}에서 성공적으로 실행되었습니다!`);
});
