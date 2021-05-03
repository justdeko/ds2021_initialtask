# delete rule
wsk -i rule delete umbrellor_clock
# delete trigger
wsk -i trigger delete interval
# delete all actions
wsk -i action delete hasher
wsk -i action delete umbrellor
wsk -i action delete helloworld