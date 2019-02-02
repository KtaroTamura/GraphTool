#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NDAT 1000
#define PI M_PI

double func(double x){
	double y;
	y=x*x;
	return y;
}

double Gauss_error(double sigma){
	double u=0;
	double x,err_try,err_ref;
	int i;
	for(i=0;i<100000;i++){
		x=10*sigma*((double)rand()/RAND_MAX-0.5);
		err_try=(double)rand()/RAND_MAX;
		err_ref=1/(sqrt(2*sigma))*exp(-1*(x-u)*(x-u)/(2*sigma*sigma));
		if(err_try<err_ref)return x;
	}
}

int main(){
	int i;
	double X,Y;
	double Y_err;
	FILE *fp;

	if((fp=fopen("sampledata.csv","w"))==NULL){
		printf("file open error!!");
	}

	for(i=0;i<NDAT;i++){
		X=0.1*i;
		Y=600+Gauss_error(sqrt(600));
//		printf("Y=%lf, Y_err=%lf \n",Y,Y_err);
		fprintf(fp,"%lf,%lf\n",X,Y);
	}

	fclose(fp);
	return 0;
}

