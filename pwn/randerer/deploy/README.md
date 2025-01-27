## 주요 포인트

`watch *0x4040b0` 으로 `canary` 값에 메모리 브레이크포인트를 걸고 실행해 봤을 때 `init_canary` 라는 함수가 이 값에 접근하고 있었는데, `init_canary` 는 `.init_array` 섹션에 등록되어 있는 함수 였음


`.init_array` 섹션은 `ELF` 바이너리에서 과거의 `.ctors` 와 비슷한 역할을 하는 섹션으로 초기화 함수들을 등록해놓음 [블로그](https://jiravvit.tistory.com/entry/main-%ED%95%A8%EC%88%98%EA%B0%80-%ED%98%B8%EC%B6%9C-%EC%A2%85%EB%A3%8C%EB%90%98%EB%8A%94-%EA%B3%BC%EC%A0%95) 에서 자세한 내용 확인
