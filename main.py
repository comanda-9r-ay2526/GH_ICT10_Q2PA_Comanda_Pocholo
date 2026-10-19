from pyscript import display, document


def namecheck(e):
    document.getElementById("result").innerHTML = " "
    Fname = document.getElementById("first").value
    Lname = document.getElementById("last").value
    FUname = Fname + Lname
    
    grade7 = {'ijicha nijiki', 'kita ikuyo', 'hitori gotoh', 'ryo yamada'}
    grade8 = {'remielle dan', 'komano manato', 'velina airgid', 'severian lowell'}
    grade9 = {'angel devil', 'shuuji taira', 'akira asai', 'rias gremory'}
    grade10 = {'mr witness', 'tomboy iskrambol', 'jb suarez', 'mohammad calaca'}

    members = (grade7 | grade8 | grade9 | grade10)
    members.add(FUname)
    
    display(f'List of members {members} amount of members {len(members)}', target='result')