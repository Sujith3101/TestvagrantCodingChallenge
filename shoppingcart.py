price={'leather wallet':1100,'umbrella':900,'cigarette':200,'honey':100}
gst={'leather wallet':.18,'umbrella':.12,'cigarette':.28,'honey':0}
quantity={'leather wallet':1,'umbrella':4,'cigarette':3,'honey':2}
total=0
for i in price:
    pric=price[i]
    if pric<500:
        gs=gst[i]
        tax=pric*gs
        final=pric+tax
    if pric>500:
        gs=gst[i]
        pri=pric-(0.05*(pric))
        tax=pri*gs
        final=pric+tax
    quan=quantity[i]
    total+=final*quan

max_gst=0
index=0
for i in price:
    pric=price[i]
    gs=gst[i]
    amt=pric*gs
    if amt>max_gst:
        max_gst=amt
        index=i
print("max gst amount paid is for product:",index)
print("total amount to be paid:",total)