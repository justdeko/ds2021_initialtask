# DS 2021 Initial Task
Initial Task for the Distributed Systems 2021 Project.

## Task 1
The first task contained setting up OpenWhisk (done in this project with k8s) and creating an action.

For this repository, openwhisk was deployed on a kubernetes cluster using kind, running on docker in a linux distribution.
### Prerequisites
- kubernetes
- docker
- kind
- openwhisk cli
- helm
### Installation
Don't forget to change the IP to your internal one inside `mycluster.yaml`.

If you're lucky enough, just run `whisk_setup.sh` in your console and whisk should be running.
If not, follow each command inside the .sh file step-by-step and troubleshoot.

After this, don't forget to connect your wsk cli: `wsk property set --apihost <INTERNAL API>:31001`

And setting auth: `wsk property set --auth 23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP`

If you don't have access for creating actions, you need to do some wskadmin magic, described [here](https://github.com/apache/openwhisk-deploy-kube#administering-openwhisk).
Also, if you get issues with the whisk CLI like "cannot validate certificate", use `wsk -i` instead of `wsk`.


Then, run `create_functions.sh` to create the two functions described below (and a helloworld for testing). Find more [here](https://github.com/apache/openwhisk/blob/master/docs/actions-python.md) on how to trigger them.

### Functions
1) Hasher: takes a "course" parameter, my name (Denis) and returns a md5 hash.
2) Umbrellor: checks the weather every 5 minutes and tells me if I should take an umbrella with me.
This is done by the following steps
   - queries [goweather](https://github.com/robertoduessmann/weather-api) based on set location
   - checks current description, if it contains "rain", return "yes" , else "no"
   - returns either "yes" or "no" with a timestamp

### Invoking the functions

An example for 1: `wsk action invoke --result hasher --param course ABC`

The umbrellor is triggered by default every 5 minutes, but this can be changed by invoking a trigger with a different parameter (e.g. duration 1 for 1 minute)

You can change this as usual, in `create_functions.sh`, as well as the default trigger city.

To check if the function is triggered properly, do ` wsk -i activation list --limit 5 umbrellor` for the last 5 activations.

To listen to the activations, do `wsk -i activation poll` in a new terminal.

### Cleanup

To delete everything, just execute `delete_everything.sh`. 

*WARNING: THIS DELETES ALL ACTIONS, TRIGGERS AND RULES*

For unmounting openwhisk itself: `helm uninstall owdev -n openwhisk`
If you want to go even one step further, delete the kind cluster: `kind delete kind`

## Task 2

The second task included completing the OpenFaaS Lab up to lab 5, as well as a custom chained function (workflow) idea with at least 4 functions,
one of them using a public API.

### Some lessons learned form the lab

- use script `openfaas_password.sh` to get the ui password, grafana is just both admin (user, password)
- use kubeforwarder instead of annyoing terminals
- if you don't want to use kubeforwarder and instead the cli, use `kubectl port-forward svc/gateway -n openfaas 8080:8080` for faas,
  and `kubectl port-forward pod/grafana 3000:3000 -n openfaas` for grafana
- use `faas-cli new --lang python3 my_function` for templates
- you can manage multiple functions in one yml, and use `faas-cli up` for building pushing and deploying.
- workshop 5 has an error, as a pod and not a deployment should be forwarded (so expose pod, not expose deployment)

### Prerequisites

- minikube or some other kubernetes thingy
- openFaas deployed on there
- faas cli also installed
- unix once again (for executing the scripts)
- ngrok setup with gateway to OpenFaas
- two instances of bots or automated workflows, one that sends a webhook to the `email-analyser` function,
one that writes an email back, coming from `email-sender`. I'm using zapier, you can obviously also use an own version.
  Or, just send a json request to the endpoint if you want to test it out.

### Main idea
Receiving bad emails is not really nice. So I decided to defend myself from those.
Each time I get an email to my account, and the sentiment analysis considers it as negative, the lights in my room flash up, 
and the sender of the email will receive a snarky response immediately. If the e-mail is neutral the sender will get a message
that I'll get back to them soon, and if it's even positive, they will get a nice compliment. If the email is really bad,
and I need additional "calming down", a function will me send a dog fact :)


### The functions

- light-machine: controls the lights in my room, lets them flash for a second based on the sentiment (good/bad/neutral)
- email-analyser: analyses the contents of my email (received as a json object), decides if its neutral, positive or negative. sends further
requests to light-machine, email-sender and cat-as-a-service
- email-sender: sends an email with a specific content depending on the sentiment
- dog-fact: returns a cut fact about dogs :)