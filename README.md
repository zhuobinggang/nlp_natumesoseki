## Usage

```py
import data_jap as data

ds = data.Dataset(half_window_size = 2)
(left, right), label = ds[0]
print(ds[0])
# ((['うとうととして目がさめると女はいつのまにか、隣のじいさんと話を始めている'], ['このじいさんはたしかに前の前の駅から乗ったいなか者である', '発車まぎわに頓狂とんきょうな声を出して駆け込んで来て、いきなり肌はだをぬいだと思ったら背中にお灸きゅうのあとがいっぱいあったので、三四郎さんしろうの記憶に残っている']), 0)
(left, right), label = ds[1]
```

