import modulos.gestoralumnos as st 
import modulos.menualumnos as ma
import modulos.agregarnotas as an
import modulos.menunotas as mn

if __name__ == '__main__':
    alumnos = {}
    
    IssAppRunning = True
    while IssAppRunning:
        op = ma.menu()
        if op == 1:
            st.AddStudent(alumnos)
        elif op == 2:
            st.DelStudent(alumnos)
        elif op == 3:
            st.DelByName(alumnos)
        elif op == 4:
            st.SearchStudent(alumnos)
        elif op == 5:
            st.ListData(alumnos)
        elif op == 6:
            isMenuNotasRunning = True
            while isMenuNotasRunning:
                opn = mn.menu()
                if opn == 1:
                    an.AddParciales(alumnos)
                elif opn == 2:
                    an.AddQuices(alumnos)
                elif opn == 3:
                    an.AddTrabajos(alumnos)
                elif opn == 4:
                    an.TablaNotas(alumnos)
                elif opn == 5:
                    an.TablaPromedios(alumnos)
                elif opn == 6:
                    isMenuNotasRunning= False
        elif op == 7:
            IssAppRunning = False
        