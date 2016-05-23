
import os
import numpy as np

ak135model = np.array([ 20.0000, 5.8000, 3.4600, 2.7200, 310., 150., 0.00, 0.00, 1.00, 1.00,
    15.0000, 6.5000, 3.8500, 2.9200, 814., 400., 0.00, 0.00, 1.00, 1.00, 
    42.5000, 8.0425, 4.4850, 3.3326, 783., 343., 0.00, 0.00, 1.00, 1.00, 
    42.5000, 8.0475, 4.4950, 3.3584, 555., 240., 0.00, 0.00, 1.00, 1.00, 
    45.0000, 8.1123, 4.5045, 3.3990, 117., 76.3, 0.00, 0.00, 1.00, 1.00, 
    45.0000, 8.2374, 4.5137, 3.3477, 122., 77.9, 0.00, 0.00, 1.00, 1.00, 
    50.0000, 8.3905, 4.5634, 3.3453, 213., 135., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 8.5726, 4.6525, 3.3886, 218., 138., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 8.7553, 4.7394, 3.4344, 224., 141., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 8.9380, 4.8263, 3.4822, 231., 145., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 9.4433, 5.1330, 3.9295, 259., 164., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 9.6114, 5.2388, 3.9253, 261., 166., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 9.7794, 5.3450, 3.9225, 263., 168., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 9.9473, 5.4513, 3.9212, 265., 170., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 10.1153, 5.5570, 3.9204, 267., 172., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 10.8562, 6.0246, 4.2687, 837., 546., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 10.9883, 6.1493, 4.3275, 818., 541., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.0953, 6.2262, 4.3842, 806., 535., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.1790, 6.2611, 4.4384, 800., 529., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.2646, 6.2981, 4.4906, 793., 524., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.3481, 6.3341, 4.5408, 787., 518., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.4299, 6.3689, 4.5790, 781., 513., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.5097, 6.4021, 4.6062, 775., 508., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.5878, 6.4348, 4.6333, 769., 503., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.6641, 6.4668, 4.6601, 763., 498., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.7393, 6.4976, 4.6868, 758., 493., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.8128, 6.5281, 4.7134, 752., 488., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.8848, 6.5579, 4.7397, 747., 483., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 11.9549, 6.5868, 4.7659, 741., 478., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.0230, 6.6147, 4.7920, 736., 474., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.0908, 6.6419, 4.8179, 730., 469., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.1579, 6.6683, 4.8435, 725., 465., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.2234, 6.6941, 4.8689, 720., 461., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.2869, 6.7196, 4.8943, 715., 457., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.3496, 6.7451, 4.9195, 710., 452., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.4119, 6.7699, 4.9445, 705., 448., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.4728, 6.7938, 4.9693, 700., 444., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.5333, 6.8172, 4.9939, 694., 440., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.5931, 6.8403, 5.0184, 686., 434., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.6516, 6.8630, 5.0427, 679., 428., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.7095, 6.8857, 5.0668, 670., 422., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.7669, 6.9083, 5.0908, 663., 417., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.8239, 6.9305, 5.1146, 659., 413., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.8808, 6.9520, 5.1382, 653., 409., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.9377, 6.9738, 5.1616, 648., 405., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 12.9944, 6.9960, 5.1848, 643., 401., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.0505, 7.0177, 5.2078, 635., 395., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.1061, 7.0395, 5.2306, 627., 390., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.1615, 7.0613, 5.2533, 621., 385., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.2179, 7.0827, 5.2758, 615., 381., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.2740, 7.1038, 5.2981, 611., 377., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.3300, 7.1256, 5.3202, 606., 374., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.3869, 7.1476, 5.3422, 600., 370., 0.00, 0.00, 1.00, 1.00, 
    49.5000, 13.4448, 7.1694, 5.3639, 595., 366., 0.00, 0.00, 1.00, 1.00, 
    48.5000, 13.5025, 7.1917, 5.3855, 590., 362., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 13.5604, 7.2142, 5.4069, 583., 357., 0.00, 0.00, 1.00, 1.00, 
    50.0000, 13.6198, 7.2369, 5.4282, 577., 353., 0.00, 0.00, 1.00, 1.00, 
    49.6699, 13.6516, 7.2539, 5.7065, 446., 273., 0.00, 0.00, 1.00, 1.00, 
    49.6602, 13.6552, 7.2646, 5.7327, 447., 274., 0.00, 0.00, 1.00, 1.00, 
    52.1699, 13.6585, 7.2758, 5.7590, 447., 274., 0.00, 0.00, 1.00, 1.00, 
    47.8301, 8.0191, 0.0000, 9.9543, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3298, 8.0830, 0.0000, 10.0332, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.1745, 0.0000, 10.1103, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.2665, 0.0000, 10.1859, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3398, 8.3559, 0.0000, 10.2598, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.4429, 0.0000, 10.3321, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.5274, 0.0000, 10.4029, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3298, 8.6092, 0.0000, 10.4720, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.6888, 0.0000, 10.5396, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.7658, 0.0000, 10.6058, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3298, 8.8397, 0.0000, 10.6704, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.9110, 0.0000, 10.7335, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 8.9798, 0.0000, 10.7952, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3398, 9.0464, 0.0000, 10.8554, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.1108, 0.0000, 10.9143, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.1733, 0.0000, 10.9718, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3298, 9.2337, 0.0000, 11.0278, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.2919, 0.0000, 11.0825, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.3482, 0.0000, 11.1359, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.4028, 0.0000, 11.1880, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3298, 9.4555, 0.0000, 11.2388, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.5059, 0.0000, 11.2883, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3401, 9.5541, 0.0000, 11.3365, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.6004, 0.0000, 11.3836, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3296, 9.6452, 0.0000, 11.4295, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.6886, 0.0000, 11.4741, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.7306, 0.0000, 11.5176, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.7713, 0.0000, 11.5600, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.8109, 0.0000, 11.6012, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.8493, 0.0000, 11.6414, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3296, 9.8866, 0.0000, 11.6805, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3403, 9.9230, 0.0000, 11.7185, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 9.9585, 0.0000, 11.7555, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3296, 9.9932, 0.0000, 11.7915, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.0271, 0.0000, 11.8265, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.0603, 0.0000, 11.8605, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.0931, 0.0000, 11.8935, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.1255, 0.0000, 11.9256, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.1577, 0.0000, 11.9568, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.1894, 0.0000, 11.9862, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3398, 10.2189, 0.0000, 12.0156, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.2447, 0.0000, 12.0452, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3301, 10.2655, 0.0000, 12.0730, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    50.3296, 10.2799, 0.0000, 12.1000, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00, 
    49.9302, 10.2872, 0.0000, 12.1262, 0.578E+05, 0.00, 0.00, 0.00, 1.00, 1.00] )

ak135Arr=ak135model.reshape(105, 10)

class Model1d(object):
    """
    An object to handle input 1d model for Computer Programs in Seismology.
    --------------------------------------------------------------------------------------------------------------
    Parameters:
    modelver           - model version
    modelname       - model name
    modelindex      - index indicating model type
                                1: 'ISOTROPIC', 2: 'TRANSVERSE ISOTROPIC', 3: 'ANISOTROPIC'
    modelunit         - KGS km, km/s, g/cm^3
    earthindex         - index indicating Earth type 1: 'FLAT EARTH', 2:'SPHERICAL EARTH'
    boundaryindex  - index indicating model boundaries 1: '1-D', 2: '2-D', 3: '3-D'
    Vindex              - index indicating nature of layer velocity
    HArr                  - layer thickness array
    VsArr, VpArr, rhoArr, QpArr, QsArr, etapArr, etasArr, frefpArr,  frefsArr
                             - model parameters
    DepthArr          - depth array
    --------------------------------------------------------------------------------------------------------------
    """
    def __init__(self, modelver='MODEL.01', modelname='TEST MODEL', modelindex=1, modelunit='KGS', earthindex=1,
            boundaryindex=1, Vindex=1, HArr=np.array([]), VsArr=np.array([]), VpArr=np.array([]), rhoArr=np.array([]),
            QpArr=np.array([]), QsArr=np.array([]), etapArr=np.array([]), etasArr=np.array([]), frefpArr=np.array([]),  frefsArr=np.array([])):
        self.modelver=modelver
        self.modelname=modelname
        modeldict={1: 'ISOTROPIC', 2: 'TRANSVERSE ISOTROPIC', 3: 'ANISOTROPIC'}
        self.modeltype=modeldict[modelindex]
        self.modelunit=modelunit
        earthdict={1: 'FLAT EARTH', 2:'SPHERICAL EARTH'}
        self.earthtype=earthdict[earthindex]
        boundarydict={1: '1-D', 2: '2-D', 3: '3-D'}
        self.boundarytype=boundarydict[boundaryindex]
        Vdict={1: 'CONSTANT VELOCITY', 2: 'VARIABLE VELOCITY'}
        self.Vtype=Vdict[Vindex]
        self.line08_11='LINE08\nLINE09\nLINE10\nLINE11\n'
        self.modelheader='H   VP  VS RHO  QP  QS ETAP ETAS FREFP FREFS'
        self.HArr=HArr
        self.VsArr=VsArr
        self.VpArr=VpArr
        self.rhoArr=rhoArr
        self.QpArr=QpArr
        self.QsArr=QsArr
        self.etapArr=etapArr
        self.etasArr=etasArr
        self.frefpArr=frefpArr
        self.frefsArr=frefsArr
        self.DepthArr=np.cumsum(self.HArr)
        return
    
    def ak135(self, modelname='AK135 CONTINENTAL MODEL'):
        """
        ak135 model
        """
        self.modelname = modelname
        self.HArr=ak135Arr[:,0]
        self.VpArr=ak135Arr[:,1]
        self.VsArr=ak135Arr[:,2]
        self.rhoArr=ak135Arr[:,3]
        self.QpArr=ak135Arr[:,4]
        self.QsArr=ak135Arr[:,5]
        self.etapArr=ak135Arr[:,6]
        self.etasArr=ak135Arr[:,7]
        self.frefpArr=ak135Arr[:,8]
        self.frefsArr=ak135Arr[:,9]
        self.DepthArr=np.cumsum(self.HArr)
        return

    def addlayer(self, H, vs, vp=None, rho=None, Qp=310., Qs=150., etap=0.0, etas=0.0, frefp=1.0, frefs=1.0,
                zmin=9999.):
        if vp ==None:
            vp=0.9409+2.0947*vs-0.8206*vs**2+0.2683*vs**3-0.0251*vs**4
        if rho==None:
            rho=1.6612*vp-0.4721*vp**2+0.0671*vp**3-0.0043*vp**4+0.000106*vp**5
        if zmin >= self.DepthArr[-1]:
            self.HArr=np.append(self.HArr, H)
            self.VpArr=np.append(self.VpArr, vs)
            self.VsArr=np.append(self.VsArr, vp)
            self.rhoArr=np.append(self.rhoArr, rho)
            self.QpArr=np.append(self.QpArr, Qp)
            self.QsArr=np.append(self.QsArr, Qs)
            self.etapArr=np.append(self.etapArr, etap)
            self.etasArr=np.append(self.etasArr, etas)
            self.frefpArr=np.append(self.frefpArr, frefp)
            self.frefsArr=np.append(self.frefsArr, frefs)
            self.DepthArr=np.cumsum(self.HArr)
        elif zmin < self.DepthArr[0]:
            continue here
            
        
        
    
    def write(self, outfname, fmt='%g'):
        """
        Write profile to the Computer Programs in Seismology model format
        """
        with open(outfname, 'w') as f:
            f.write(self.modelver+'\n')
            f.write(self.modelname+'\n')
            f.write(self.modeltype+'\n')
            f.write(self.modelunit+'\n')
            f.write(self.earthtype+'\n')
            f.write(self.boundarytype+'\n')
            f.write(self.Vtype+'\n')
            f.write(self.line08_11)
            f.write(self.modelheader+'\n')
            for i in np.arange(self.HArr.size):
                tempstr='%f %f %f %f %f %f %f %f %f %f \n' %(self.HArr[i], self.VpArr[i], self.VsArr[i], self.rhoArr[i],
                        self.QpArr[i], self.QsArr[i], self.etapArr[i], self.etasArr[i], self.frefpArr[i], self.frefsArr[i])
                # tempstr=fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt+' '+fmt + ' \n' %(self.HArr[i], self.VpArr[i], self.VsArr[i], self.rhoArr[i],
                #         self.QpArr[i], self.QsArr[i], self.etapArr[i], self.etasArr[i], self.frefpArr[i], self.frefsArr[i])
                f.write(tempstr)
        return
            
    def read(self, infname, sep='\t'):
        """
        Read Computer Programs in Seismology model format
        """
        with open(infname, 'r') as f:
            self.modelver=(f.readline()).split('\n')[0]
            self.modelname=(f.readline()).split('\n')[0]
            self.modeltype=(f.readline()).split('\n')[0]
            self.modelunit=(f.readline()).split('\n')[0]
            self.earthtype=(f.readline()).split('\n')[0]
            self.boundarytype=(f.readline()).split('\n')[0]
            self.Vtype=(f.readline()).split('\n')[0]
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            self.modelheader=(f.readline()).split('\n')[0]
            for line in f.readlines():
                cline=line.split()
                self.HArr=np.append(self.HArr, float(cline[0]))
                self.VpArr=np.append(self.VpArr, float(cline[1]))
                self.VsArr=np.append(self.VsArr, float(cline[2]))
                self.rhoArr=np.append(self.rhoArr, float(cline[3]))
                self.QpArr=np.append(self.QpArr, float(cline[4]))
                self.QsArr=np.append(self.QsArr, float(cline[5]))
                self.etapArr=np.append(self.etapArr, float(cline[6]))
                self.etasArr=np.append(self.etasArr, float(cline[7]))
                self.frefpArr=np.append(self.frefpArr, float(cline[8]))
                self.frefsArr=np.append(self.frefsArr, float(cline[9]))
        return
    
    def perturb(self, dm, zmin=-9999, zmax=9999, datatype='vs'):
        index=(self.DepthArr<zmax) * (self.DepthArr>zmin)
        print index
        if datatype=='vp':
            self.VpArr[index]=self.VpArr[index]*(1.+dm)
        if datatype=='vs':
            print self.VsArr[index]*(1.+dm)
            self.VsArr[index]=self.VsArr[index]*(1.+dm)
        if datatype=='rho':
            self.rhoArr[index]=self.rhoArr[index]*(1.+dm)
        if datatype=='qp':
            self.QpArr[index]=self.QpArr[index]*(1.+dm)
        if datatype=='qs':
            self.QsArr[index]=self.QsArr[index]*(1.+dm)
        if datatype=='etap':
            self.etapArr[index]=self.etapArr[index]*(1.+dm)
        if datatype=='etas':
            self.etasArr[index]=self.etasArr[index]*(1.+dm)
        if datatype=='frefp':
            self.frefpArr[index]=self.frefpArr[index]*(1.+dm)
        if datatype=='frefs':
            self.frefsArr[index]=self.frefsArr[index]*(1.+dm)
        ztop=self.DepthArr[index][0]
        zbottom=self.DepthArr[index][-1]
        print 'Top:', ztop, 'km Bottom:', zbottom,'km'
        return
    
    

        
    
 