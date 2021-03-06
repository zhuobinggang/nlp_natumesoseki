import random

def read_docs():
  filenames = ['sansirou', 'sorekara', 'mon', 'higan', 'gyoujin']
  paths = [f'datasets/{name}_new.txt' for name in filenames]
  docs = []
  for path in paths:
    with open(path) as f:
      lines = f.readlines()
      docs.append(lines)
  return docs

def read_lines():
  docs = read_docs()
  lines = []
  for doc in docs:
    lines += doc
  return [line.replace(' ', '').replace('\n', '') for line in lines]

def read_sentences():
  lines = read_lines()
  sentences = []
  for line in lines:
    ss = line.split('。')
    for s in ss:
      if len(s) > 1:
        sentences.append(s)
  return sentences

def read_trains():
  ss = read_sentences()
  return ss

def no_indicator(ss):
  return [s.replace('\u3000', '') for s in ss]

class Dataset():
  def __init__(self, half_window_size = 1):
    self.init_datas_hook()
    self.half_window_size = half_window_size

  def init_datas_hook(self):
    self.datas = read_trains()

  def __len__(self):
    return len(self.datas)

  def __getitem__(self, idx):
    if idx >= len(self.datas) - 1:
      print(f'Warning: Should not get idx={idx}')
      return None
    left = []
    start = max(0, idx + 1 - self.half_window_size)
    end = min(idx + 1, len(self.datas))
    for i in range(start, end):
      left.append(self.datas[i])
    right = []
    start = max(0, idx + 1)
    end = min(idx + 1 + self.half_window_size, len(self.datas))
    for i in range(start, end):
      right.append(self.datas[i])
    label = 1 if right[0].startswith('\u3000') else 0
    left = no_indicator(left)
    right = no_indicator(right)
    return (left,right), label

  def shuffle(self):
    random.shuffle(self.datas)

