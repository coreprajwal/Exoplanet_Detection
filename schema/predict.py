from pydantic import BaseModel

class PredictRequest(BaseModel):
       koi_score: float
       koi_fpflag_nt: float
       koi_fpflag_ss: float
       koi_fpflag_co: float
       koi_fpflag_ec: float
       koi_period: float
       koi_time0bk: float
       koi_impact: float
       koi_duration: float
       koi_depth: float
       koi_prad: float
       koi_teq: float
       koi_insol: float
       koi_model_snr: float
       koi_tce_plnt_num: float
       koi_steff: float
       koi_steff_err1: float
       koi_steff_err2: float
       koi_slogg: float
       koi_slogg_err1: float
       koi_slogg_err2: float
       koi_srad: float
       ra: float
       dec: float
       koi_kepmag: float
       koi_pdisposition_int: float
       koi_tce_delivname_q1_q17_dr24_tce: float
       koi_tce_delivname_q1_q17_dr25_tce: float
       
class PredictResponse(BaseModel):
       label:str
       confidence:float