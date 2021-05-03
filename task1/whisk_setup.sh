# Create kind cluster
kind create cluster --config kind-cluster.yaml
# Label two worker nodes (invoker, rest of openwhisk)
kubectl label node kind-worker openwhisk-role=core
kubectl label node kind-worker2 openwhisk-role=invoker
# add helm repo and install
helm repo add openwhisk https://openwhisk.apache.org/charts
helm repo update
helm install owdev openwhisk/openwhisk -n openwhisk --create-namespace -f mycluster.yaml