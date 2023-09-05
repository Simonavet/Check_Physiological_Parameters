from the_application.check_parameters import *

horse = Horse()
cow = Bovine()
dog = Dog()
cat = Cat()
guinea_pig = Guinea_pig()
lion = Lion()
llama = Llama()

print('Name specie')
x = str(input())

if x == 'horse':
    print(f'Respiratory rate: '), horse.horse_respiration(hr=int(input()))
    print(f'Heart beat: '), horse.horse_heart_beat(hhb=int(input()))
    print(f'Temperature: '), horse.horse_temperature(ht=float(input()))

elif x == 'cow':
    print(f'Respiratory rate: '), cow.bovine_respiration(br=int(input()))
    print(f'Heart beat: '), cow.bovine_heart_beat(bhb=int(input()))
    print(f'Temperature: '), cow.bovine_temperature(bt=float(input()))

elif x == 'dog':
    print(f'Respiratory rate: '), dog.dog_respiration(dr=int(input()))
    print(f'Heart beat: '), dog.dog_heart_beat(dhb=int(input()))
    print(f'Temperature: '), dog.dog_temperature(dt=float(input()))

elif x == 'cat':
    print(f'Respiratory rate: '), cat.cat_respiration(cr=int(input()))
    print(f'Heart beat: '), cat.cat_heart_beat(chb=int(input()))
    print(f'Temperature: '), cat.cat_temperature(ct=float(input()))


elif x == 'guinea pig':
    print(f'Respiratory rate: '), guinea_pig.guinea_pig_respiration(gpr=int(input()))
    print(f'Heart beat: '), guinea_pig.guinea_pig_heart_beat(gphb=int(input()))
    print(f'Temperature: '), guinea_pig.guinea_pig_temperature(gpt=float(input()))

elif x == 'lion':
    print(f'Respiratory rate: '), lion.lion_respiration(lr=int(input()))
    print(f'Heart beat: '), lion.lion_heart_beat(lhb=int(input()))
    print(f'Temperature: '), lion.lion_temperature(lt=float(input()))

elif x == 'llama':
    print(f'Respiratory rate: '), llama.llama_respiration(llr=int(input()))
    print(f'Heart beat: '), llama.llama_heart_beat(llhb=int(input()))
    print(f'Temperature: '), llama.llama_temperature(llt=float(input()))

else:
    print('I do not know this specie')


