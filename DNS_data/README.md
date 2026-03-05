The directory contains the DNS data used in the present study. The DNS data files follow the naming convention:

#
data[$Re_{\tau}$]_[$Ri_{\tau}$].csv
#


where $Re_{\tau}$ is the friction Reynolds number, and $Ri_{\tau}$ is the friction Richardson number.

### Variables

Each CSV file contains simulation data sampled from the DNS results. The columns represent the following variables;
#
[
    `zc`, `zf`, `zp_c`, `rc`, `ruc`,
    `ruwc`, 
    `sc`, `umc`, `vmc`, `wmc`, `umf`, `vmf`, `wmf`,
    `muc`, `kthc`, `muf`, `kthf`, `rf`, `dzc`, `dzf`,
    `tau13c`, `tau13f`
]
#

where


| Variable | Description |
|---------|-------------|
| `zc` | Wall-normal coordinate at the cell center |
| `zf` | Wall-normal coordinate at the cell face |
| `zp_c` | Wall-normal coordinate scaled by the viscous length scale |
| `rc` | Density at the cell center |
| `ruc` | Density weighted velocity (ρu) at the cell center |
| `ruwc` | Reynolds shear stress (ρuw) at the cell center |
| `sc` | Temperature at the cell center |
| `umc` | Reynolds averaged streamwise velocity at the cell center |
| `vmc` | Reynolds averaged spanwise velocity at the cell center |
| `wmc` | Reynolds averaged wall-normal velocity at the cell center |
| `umf` | Reynolds averaged streamwise velocity at the cell face |
| `vmf` | Reynolds averaged spanwise velocity at the cell face |
| `wmf` | Reynolds averaged wall-normal velocity at the cell face |
| `muc` | Dynamic viscosity at the cell center |
| `muf` | Dynamic viscosity at the cell face |
| `kthc` | Thermal conductivity at the cell center |
| `kthf` | Thermal conductivity at the cell face |
| `rf` | Density at the cell face |
| `dzc` | Grid spacing at the cell center |
| `dzf` | Grid spacing at the cell face |
| `tau13c` | Shear stress component at the cell center |
| `tau13f` | Shear stress component at the cell face |



An example post-processing script is included in the repository (`post_public.ipynb`). It generates plots of the mean velocity profile in different flow regions and evaluates the deviation between the coefficient of friction predicted by the model and the values obtained from DNS.