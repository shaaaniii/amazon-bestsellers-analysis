#include<iostream>
using namespace std;

class sphere
{
	private:
	double radius,volume,surface_area;
	 public:
	 class cuboid
	 {
		 private:
			double length,width,height,vol,surface_area;
			
			public:
			void Accept(){
				cout<<"enter the length of cuboid:";
				cin>>length;
				cout<<"enter the width of cuboid:";
				cin>>width;
				cout<<"enter the height of cuboid:";
				cin>>height;
			}
			
			void CAL_volume(){
            vol=length*width*height;
		}
		void cal_surfacearea(){
			surface_area=2*(length*width+width*height+height*length);
		}
		void display_data(){
			cout<<" volume of cuboid:"<<vol<<"cubic cm"<<endl;
			cout<<"surface area of cuboid:"<<surface_area<<"sq cm"<<endl;
		}
	};
	
		 
	 void Accept(){
		 cout<<"enter the radius of sphere:";
		 cin>>radius;
	 }
	 
	 void Cal_volume(){
		volume=4*3.14*radius*radius*radius/3;
	}
	
	void cal_surface(){
		surface_area=4*3.14*radius*radius;
	}
	void display(){
		cout<<"volume of sphere is:"<<volume<<"cubic cm"<<endl;
		cout<<"surface area of sphere is :"<<surface_area<<"sq cm"<<endl;
	}
	
};
int main(){
	sphere r1;
	sphere::cuboid c1;
	r1.Accept();
	r1.Cal_volume();
	r1.cal_surface();
	c1.Accept();
	c1.CAL_volume();
	c1.cal_surfacearea();
	r1.display();
	c1.display_data();
	
	
	
	return 0;
}
			
			
			
			
			
			
			
			
			
		
		
		
		
		 
