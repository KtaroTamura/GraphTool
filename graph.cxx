int graph(){
	double x,y;
	int i=0;
	FILE *fp;

	fp=fopen("sampledata.csv","r");
	TGraph *g1=new TGraph();
	while((fscanf(fp,"%lf,%lf",&x,&y))!=EOF){
		g1->SetPoint(i,x,y);
		i++;
	}

	g1->Draw();
	fclose(fp);
	return 0;
}
