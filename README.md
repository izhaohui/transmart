# Summery

1. this package is used for transfer file between computer and mobile devices(Like qr-transfer)
2. the package contains two executable files, one for send file from PC, another for proxy the transfer when your mobile can not reach your PC direct(In different network).
3. you need a server to deploy the proxy script, and config the proxy ip in your client config.

# Config

## Install
Install transmart on both PC and your server.
* Server
    
    run `transproxy -p` get proxy url, remember replace with your real ip(default 0.0.0.0 can not work).
    
    run `systemctl start transproxy`
    
    
* PC

    run `transmart -i` get {identity}
    
    run `transmart -p {server_uri}` to set proxy uri
    
    run `transproxy -a {identity}` on server to add you PC to server trust list.

