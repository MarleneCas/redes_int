from random import random
from simulation import Simulation
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # 1 simulation 
    simulation = Simulation(
        mesageDifs=10e-3,
        mesageSifs=5e-3,
        mesageRts=11e-3,
        mesageCts=11e-3,
        mesageAck=11e-3,
        mesageData=43e-3,
        num_nodos=5,
        ranuSleeping=18,
        max_mini_ranuras=16,
        lambda_pkt=0.0005,
        size_buffer=15,
        num_grades=7,
        sigma=1e-3,
        #No se si poner aquí U esta bien, pero intente ponerla en la simulation pero me daba siempre cero 
        #var_u= 1**6*random()/1**6,
    )
    # 2 corres metodo 
    simulation.ini_sim()
    
    # 3 obtienes through
    resThroug = simulation.get_pkt_ciclo_throughtput()
    
    # 1 simulation 
    simulation1 = Simulation(
        mesageDifs=10e-3,
        mesageSifs=5e-3,
        mesageRts=11e-3,
        mesageCts=11e-3,
        mesageAck=11e-3,
        mesageData=43e-3,
        num_nodos=5,
        ranuSleeping=18,
        max_mini_ranuras=16,
        lambda_pkt=0.005,
        size_buffer=15,
        num_grades=7,
        sigma=1e-3,
        #No se si poner aquí U esta bien, pero intente ponerla en la simulation pero me daba siempre cero 
        #var_u= 1**6*random()/1**6,
    )
    # 2 corres metodo 
    simulation1.ini_sim()
    
    # 3 obtienes through
    resThroug1 = simulation1.get_pkt_ciclo_throughtput()
    
    # 1 simulation 
    simulation2 = Simulation(
        mesageDifs=10e-3,
        mesageSifs=5e-3,
        mesageRts=11e-3,
        mesageCts=11e-3,
        mesageAck=11e-3,
        mesageData=43e-3,
        num_nodos=5,
        ranuSleeping=18,
        max_mini_ranuras=16,
        lambda_pkt=0.001,
        size_buffer=15,
        num_grades=7,
        sigma=1e-3,
        #No se si poner aquí U esta bien, pero intente ponerla en la simulation pero me daba siempre cero 
        #var_u= 1**6*random()/1**6,
    )
    # 2 corres metodo 
    simulation2.ini_sim()
    
    # 3 obtienes through
    resThroug2 = simulation2.get_pkt_ciclo_throughtput()

    # 1 simulation 
    simulation3 = Simulation(
        mesageDifs=10e-3,
        mesageSifs=5e-3,
        mesageRts=11e-3,
        mesageCts=11e-3,
        mesageAck=11e-3,
        mesageData=43e-3,
        num_nodos=5,
        ranuSleeping=18,
        max_mini_ranuras=16,
        lambda_pkt=0.03,
        size_buffer=15,
        num_grades=7,
        sigma=1e-3,
        #No se si poner aquí U esta bien, pero intente ponerla en la simulation pero me daba siempre cero 
        #var_u= 1**6*random()/1**6,
    )
    # 2 corres metodo 
    simulation3.ini_sim()
    
    # 3 obtienes through
    resThroug3 = simulation3.get_pkt_ciclo_throughtput()




    listLambda = [0.0005,0.005,0.001,0.03]
    listThrough = [resThroug,resThroug1,resThroug2,resThroug3]
    
    plt.plot(listLambda,listThrough)
    plt.show()
    plt.xlabel('grados')
    plt.ylabel('Ppaquetes/ciclo')
    plt.title('throughput')

    """
    for i in range(300):
        simulation.generating_pkt_ramdom_grade_and_node()

    for i in range(6,-1,-1):
        print(i)
        simulation.transmit_pkt_to_next_grade(i)

    """
    simulation.print_network()


    #for i in range(0,40):
        #simulation.generating_pkt_ramdom_grade_and_node()
    #for i in range(6):
        #print("fasdfs")
        #for num_grade in range(6,-1,-1):
            #simulation.transmit_pkt_to_next_grade(num_grade)

