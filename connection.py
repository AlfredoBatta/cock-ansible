import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

for server in conn.list_servers():
    print(server.to_dict())
