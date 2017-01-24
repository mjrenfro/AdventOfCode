#most frequent ele got from SO
lines=zip(*([l.strip() for l in open('p6input.txt').readlines()]))
print ("".join(map(lambda lst: max(set(lst), key=lst.count), lines)))
