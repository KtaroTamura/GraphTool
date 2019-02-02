int hist(){
	double x,y;
	FILE *fp;

	fp=fopen("sampledata.csv","r");
	TH1D *h1=new TH1D("h1","h1title",200,500,700);
	while((fscanf(fp,"%lf,%lf",&x,&y))!=EOF){
		h1->Fill(y);
	}

	fclose(fp);
	h1->Draw();
	return 0;
}
