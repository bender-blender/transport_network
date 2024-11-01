from transport import Car,Bicycle,Motorcycle
from interface import ITransport
from factory import Factory





def client_code(transport:ITransport):
    a = Factory(transport).create_transport()
    a.start_engine()
    a.stop_engine()

lst = [Car,Bicycle,Motorcycle] 
for i in lst:
    client_code(i)