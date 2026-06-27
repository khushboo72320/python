losses=[0.95,-0.78,0.65,-0.765]
losses.append(0.19)
losses.append([0.18,0.20])
print("append",(losses))

#extend
losses=[0.95,-0.72,0.45,-0.31]
list2=[1,2,3]
losses.extend(list2)
losses.append(0.18)
print("extend",(losses))

#sorted.py
scores=[1,9,6,4]
sorted_scores=sorted(scores)
print(sorted_scores)

#score.sort
scores=[1,8,4,0]
sorted_scores=sorted(scores)
print(sorted_scores)
scores.sort(reverse=True)
print (scores)

#outlier
predictions=[8.8,90,9.7,68,-89]
remove=predictions.remove(-89,)
print(predictions)

#2 outliers remove
predictions=[8.8,-99,-99,-0.67,90,9.7,68]
sorted_list=sorted(predictions)
print (sorted_list)
outlier=sorted_list[0]
while outlier in predictions:
  predictions.remove(outlier)
print(predictions)

#tupple

image_shape=(356,897,67)
print(type(image_shape))

#add in tuple
image_shape=[356,897,67]
list1=list(image_shape)
list1.append(5)
list2.append(6)
image_shape=tuple(list1)
print(image_shape)

#unpacking tuple
image_shape=[1,2,3]
h,w,c=image_shape
print(f"height:{h},width:{w},channels:{c}")


#wildcard unpacking
dataset_record=("sample_0.42",0.95,0.04,0.01,"positive_class")
sample_id,*probabilities,label=dataset_record
print(sample_id)
print(probabilities)
print(label)


#dictionaries in action
config={"modal_type":"randomforst",
        "n_estimators":100,
        "max_depth":10,
        "random_state":42
        }
print(type(config["max_depth"]))
config["max_depth"]=20

#
config={"modal_type":"randomforst",
        "n_estimators":100,
        "max_depth":10,
        "random_state":42 
}
for key,values in config.items():
              print(key,values)

#sets in action
train_class={"cat","dog","bird","cat"}
val_classes={"dog","horse","sheep"}
print(type(train_class))   
# set

list1=[23,54,67,89]
new_set=set(list1)
print (new_set)
list1=list(new_set)
#print ("unique elements are:"list1)

#union

train_classes={"cat","dog","bird","cat"}
val_classes={"dog","horse","sheep"}
all_clases= train_classes | val_classes
all_classes=train_classes.union(val_classes)
print(f"all classes:{all_classes}")

#intesection
train_classes={"cat","dog","bird","cat"}
val_classes={"dog","horse","sheep"}
only_train=train_classes &val_classes
all_classes=train_classes.intersection(val_classes)
print(f"all classes:{all_classes}")

