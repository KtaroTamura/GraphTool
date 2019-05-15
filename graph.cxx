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

///Graph Setting///
//  g1->SetTitle("Title");
//	g1->GetXaxis()->SetTitle("XX");
//	g1->GetYaxis()->SetTitle("YY");

	g1->Draw();
	fclose(fp);
	return 0;
}
