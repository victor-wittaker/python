with open('ips.txt', 'r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        octetos = i.split('.')
        
        if len(octetos) == 4:
            for oc in octetos:
                if int(oc) < 0 or int(oc) > 255:
                    break
            else:
                with open('ips-validos.txt', 'a') as fi:
                    fi.write(i + '\n')
