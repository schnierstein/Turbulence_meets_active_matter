#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <complex.h>
#include <vector>
#include <math.h>
#include <string>
#include <eigen3/Eigen/Dense>
#include <random>
#include <time.h>
#include <chrono>
#include <thread>
#include <future>
#include <new>
#include <fftw3.h>

using namespace std;
using namespace Eigen;
const int N = 10,
          kmax = 5;

const double  dt = 0.005,
              t_max = 100,
              h = 1./N;


int main(int argc, char const *argv[]) {
  Matrix<double,Dynamic,Dynamic> T(N,N);
  Matrix<double,Dynamic,Dynamic> k_xx(N,N);
  Matrix<double,Dynamic,Dynamic> k_yy(N,N);

  for(int i=0; i < N; i++){
    for(int j=0; j < N; j++){
      k_xx(i,j) = (((double) j)/N) * kmax;
      k_yy(i,j) = (((double) i)/N) * kmax;
      T(i,j) = exp(-(pow(i-N/2.,2)+pow(j-N/2.,2)));
    }
  }
  cout << k_xx << endl << k_yy << endl << T << endl;




  return 0;
}
