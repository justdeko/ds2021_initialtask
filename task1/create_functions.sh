# create actions
wsk -i action create hasher hasher.py
wsk -i action create umbrellor umbrellor.py
wsk -i action create helloworld helloworld.py
# Create umbrellor trigger and rule
wsk -i trigger create interval \
  --feed /whisk.system/alarms/interval \
  --param minutes 5 \
  --param trigger_payload "{\"city\":\"Berlin\"}" \
  --param stopDate "2021-05-10T23:59:00.000Z"
# check updates, create rule that connects umbrellor to periodic trigger
wsk -i trigger update interval
wsk -i action update umbrellor umbrellor.py
wsk -i rule create umbrellor_clock interval umbrellor