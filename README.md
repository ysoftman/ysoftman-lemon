# github 을 pip 패키지로 설치하기

## build this test

```bash
# pip => pip3(python3)
# local 에서 설치
pip install .

# github에서 기준으로 설치
pip install git+https://github.com/ysoftman/ysoftman-lemon

# 설치 확인
pip list | grep ysoftman_lemon

# 사용하기
python lemon_test.py
```
