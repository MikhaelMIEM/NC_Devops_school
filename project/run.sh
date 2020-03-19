nginx_conf_path=./load_balancer/nginx.conf
nginx_template_path=./load_balancer/nginx_conf_template

if [ -z $1 ]; then
        replicas_num=1
else
        replicas_num=$1
fi
echo started with replicas amount $replicas_num

servers_string=''
for (( i=1; i<=$replicas_num; i++))
do
        servers_string=$servers_string"server project_backend_server_$i:10000;\n\t\t"
done

sed -e "s/\${servers}/${servers_string}/g" $nginx_template_path > $nginx_conf_path


docker-compose build
docker-compose up --scale backend_server=$replicas_num

