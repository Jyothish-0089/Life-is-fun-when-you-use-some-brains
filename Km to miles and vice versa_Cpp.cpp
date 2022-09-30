//Write a program in C++ that converts kilometers per hour to miles per hour.
#include<iostream>
using namespace std;
int main(){
	int km,m,choice;
	cout<<"1-Convert to Miles per hour\n";
	cout<<"2-Convert to Kilometre per hour\n";
	cin>>choice;
	if(choice==1){
		cout<<"Enter speed in kilometre per hour : ";
		cin>>km;
		float m = km*1.60;
		cout<<"\n"<<km<<" Km/hr = "<<m<<" Miles/hr";
	}
	else{
		if(choice==2){
			cout<<"Enter speed in miles per hour : ";
			cin>>m;
			float km = 0.621*m;
			cout<<"\n"<<m<<" Miles per hr = "<<km<<" Km per hr";
		}
		else{
			cout<<"You had one job...Just enter 1 or 2 man..";
    	}
	}
	return 0;
}
