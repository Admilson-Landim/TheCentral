

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct patient {
    int bi;
    char name[20];
    char email[30];
    int age;
    char address[30];
    char contact[20];
};

struct doctor {
    int bi;
    char name[50];
    char specialty[50];
    char contact;
    char email[50];
    char address[100];
};

struct patient patients[100];
int patientCount = 0;
struct doctor doctors[100];
int doctorCount = 0;


void addPatient() {
    struct patient newPatient;
    int i, j;
    
    printf(" BI do paciente: ");
    //scanf("%d", &newPatient.bi);
    // validar insercao de apenas numeros em Contacto.....
    while(1){
    	if(scanf("%d", &newPatient.bi)==1 && newPatient.bi>0) break;
     	printf(" BI invalida, digite BI: ");
      	fflush(stdin);
    }
    
    // validar se bi ja existe.....
    for (i = 0; i < patientCount; i++) {
        if (patients[i].bi == newPatient.bi) {
            printf("Paciente com BI %d ja existe\n", newPatient.bi);
            return;
        }
    }
    printf(" Name: ");
    scanf("%s", newPatient.name);
    
    printf(" Email: ");
    scanf("%s", newPatient.email);
    
    printf(" Idade: ");
    //scanf("%d", &newPatient.age);
    // validando idade
    while(1){
    	if(scanf("%d", &newPatient.age)==1 && newPatient.age>0) break;
     	printf(" Idade invalida, digite numero: ");
      	fflush(stdin);
    }
    
    printf(" Morada: ");
    scanf("%s", newPatient.address);
    
    printf(" Contacto: ");
    scanf("%s", newPatient.contact);
    
    patients[patientCount] = newPatient;
    patientCount++;
    printf("Pacient adicionado com sucesso !!! \n");
}

void editPatient() {
    int bi, i;
    printf("Enter paciente BI: ");
    scanf("%d", &bi);
    for (i = 0; i < patientCount; i++) {
        if (patients[i].bi == bi) {
            printf("NOvo Nome: ");
		    scanf("%s", patients[i].name);
		    
		    printf("Novo Email: ");
		    scanf("%s", patients[i].email);
		    
		    printf("Nova Idade: ");
		    //scanf("%d", &patients[i].age);
		    // validando idade
		    while(1){
		    	if(scanf("%d", &patients[i].age)==1 && (&patients[i].age)>0) break;
		     	printf(" Idade invalida, digite numero: ");
		      	fflush(stdin);
		    }
		    
		    printf("Nova Morada: ");
		     scanf("%s", patients[i].address);
		    
		    printf("Novo Contacto: ");
		    scanf("%s", patients[i].contact);
		    
            printf("Paciente editadu com sucesso....\n");
            return;
        }
    }
    printf("Paciente nao encontrado....\n");
}

void deletePatient() {
    int bi, i, j;
    printf("BI: ");
    scanf("%d", &bi);
    for (i = 0; i < patientCount; i++) {
        if (patients[i].bi == bi) {
            for (j = i; j < patientCount - 1; j++) {
                patients[j] = patients[j + 1];
            }
            patientCount--;
            printf("Paciente deletado com successo... \n");
            return;
        }
    }
    printf("Paceient nao encontrado !!!\n");
}

void listPatients() {
    int i;
    printf("BI\t\t | Nome\t\t | Email\t\t\t | Idade\t | Morada\t\t | Contacto |\n");
    for (i = 0; i < patientCount; i++) {
        printf("%d\t\t | %s\t\t | %s\t\t\t | %d\t\t | %s\t\t | %s |\n", patients[i].bi, patients[i].name, patients[i].email, patients[i].age, patients[i].address, patients[i].contact);
    }
}

void searchPatientByBI() {
    int i, bi;
    printf("BI: ");
    scanf("%d", &bi);
    for (i = 0; i < patientCount; i++) {
        if (patients[i].bi == bi) {
            printf("Nome: %s\n", patients[i].name);
            printf("Email: %s\n", patients[i].email);
            printf("Idade: %d\n", patients[i].age);
            printf("Morada: %s\n", patients[i].address);
            printf("Contacto: %s\n", patients[i].contact);
            return;
        }
    }
    printf("Paciente com BI %d nao encontrado !!!", bi);
}



void addDoctor() {
    struct doctor newDoctor;
   
    printf("BI: ");
    //scanf("%s", newDoctor.bi);
     while(1){
    	if(scanf("%d", &newDoctor.bi)==1 && &newDoctor.bi>0) break;
     	printf(" BI invalido, digite BI: ");
      	fflush(stdin);
    }
    
    printf("Nome: ");
    scanf("%s", newDoctor.name);
    
    printf("Especialidade: ");
    scanf("%s", newDoctor.specialty);
    
    //printf("Comtacto: ");
    //scanf("%s", newDoctor.contact);
   
    printf("Email: ");
    scanf("%s", newDoctor.email);
    
    printf("Morada: ");
    scanf("%s", newDoctor.address);
    
    doctors[doctorCount] = newDoctor;
    doctorCount++;
    printf("Doctor adicionado com sucesso...\n");
}

void removeDoctor() {
    int i, bi;
    printf("BI: ");
    scanf("%d", &bi);
    for (i = 0; i < doctorCount; i++) {
        if (doctors[i].bi == bi) {
            doctors[i] = doctors[doctorCount - 1];
            doctorCount--;
            printf("Doctor removido com successo...\n");
            return;
        }
    }
    printf("Doctor com BI %d nao encontrado\n", bi);
}

void listDoctors() {
    int i;
    for (i = 0; i < doctorCount; i++) {
        printf("BI: %d\n", doctors[i].bi);
        printf("Nome: %s\n", doctors[i].name);
        printf("Especialidade: %s\n", doctors[i].specialty);
        printf("Contacto: %d\n", doctors[i].contact);
        printf("Email: %s\n", doctors[i].email);
       	printf("Morada: %s\n", doctors[i].address);
        printf("\n");
    }
}

void editDoctor() {
    int i, bi;
    printf("Editar Doctor com BI: ");
    scanf("%d", &bi);
    for (i = 0; i < doctorCount; i++) {
        if (doctors[i].bi == bi) {
            printf("Nome novo: ");
            scanf("%s", doctors[i].name);
            printf("Especialidade novo: ");
            scanf("%s", doctors[i].specialty);
            printf("Contacto novo: ");
            scanf("%d", &doctors[i].contact);
            printf("Email novo: ");
            scanf("%s", doctors[i].email);
            printf("Morada novo: ");
            scanf("%s", doctors[i].address);
            printf("Doctor editado com successo....\n");
            return;
        }
    }
    printf("Doctor with BI %d not found\n", bi);
}

void searchDoctorByBI() {
    int i, bi;
    printf("Enter doctor BI: ");
    scanf("%d", &bi);
    for (i = 0; i < doctorCount; i++) {
        if (doctors[i].bi == bi) {
            printf("DNome: %s\n", doctors[i].name);
            printf("Especialidade: %s\n", doctors[i].specialty);
            printf("Contacto: %d\n", doctors[i].contact);
            printf("Email: %s\n", doctors[i].email);
            printf("Morada: %s\n", doctors[i].address);
            return;
        }
    }
    printf("Doctor com BI %d nao encontrado\n", bi);
}









int main() {
    int option;
    do {
    	printf("*************************************************************\n");
    	printf("********************* MENU OPTIONS:    **********************\n");
    	printf("*************************************************************\n");
        printf("1  --  Adicionar paciente                                   *\n");
        printf("2  --  Editar paciente                                      *\n");
        printf("3  --  Deletar paciente                                     *\n");
        printf("4  --  Lista pacients                                       *\n");
        printf("5  --  Pesquisar paciente                                   *\n");
        printf("------------------------------------------------------------*\n");
        printf("6  --  Adicionar Medico                                     *\n");
        printf("7  --  Editar Medico                                        *\n");
        printf("8  --  Deletar Medico                                       *\n");
        printf("9  --  Lista Medico                                         *\n");
        printf("10 --  Pesquisar Medico                                     *\n");
        printf("------------------------------------------------------------*\n");
        printf("15  --  SAir                                                *\n");
        printf("Escolha uma opcao::: ");
        scanf("%d", &option);
        printf("\n");
        switch (option) {
        	// Paciente
        	case 1: addPatient(); break;
            case 2: editPatient(); break;
            case 3: deletePatient(); break;
            case 4: listPatients(); break;
            case 5: searchPatientByBI(); break;
            
            // Medico
            case 6: addDoctor(); break;
            case 7: editDoctor(); break;
            case 8: removeDoctor(); break;
            case 9: listDoctors(); break;
            case 10: searchDoctorByBI(); break;
            
            // Outros casos
            case 15: break;
            default: printf("Opcao Invalido !!!\n"); break;
        }
        printf("\n\n");
    } while (option != 15);
    return 0;
}

