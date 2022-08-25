
Docker-desktop

Si al ejecutar el docker-compose up obtenemos el error "ERROR: for db  Cannot start service db: Ports are not available: exposing port TCP 0.0.0.0:5432 -> 0.0.0.0:0: listen tcp 0.0.0.0:5432: bind: Intento de acceso a un socket no permitido por sus permisos de acceso" de que los puertos no son acccesibles debemos seuir estas instrucciones

https://github.com/docker/for-win/issues/3171



    Disable hyper-v (which will required a couple of restarts)
    dism.exe /Online /Disable-Feature:Microsoft-Hyper-V

    When you finish all the required restarts, reserve the port you want so hyper-v doesn't reserve it back
    netsh int ipv4 add excludedportrange protocol=tcp startport=5432y numberofports=1

    Re-Enable hyper-V (which will require a couple of restart)
    dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
