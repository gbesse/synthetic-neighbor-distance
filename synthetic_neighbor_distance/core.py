from .common import number,unique_ids
def run(data):
 source=data['source'];synthetic=data['synthetic'];scales=[number(x,1e-12,1e12)for x in data['scales']];threshold=number(data.get('near_threshold',.05),0,1e6)
 if not 1<=len(scales)<=30 or not 1<=len(source)<=1000 or len(synthetic)>1000:raise ValueError('sizes')
 unique_ids(source);unique_ids(synthetic)
 for row in source+synthetic:
  if len(row['values'])!=len(scales):raise ValueError('width')
  for v in row['values']:number(v,-1e12,1e12)
 output=[]
 for row in synthetic:
  distances=[(sum(abs(a-b)/s for a,b,s in zip(row['values'],r['values'],scales))/len(scales),r['id'])for r in source];best=min(d for d,_ in distances);ties=[key for d,key in distances if d==best]
  output.append({'id':row['id'],'nearest_distance':best,'nearest_source_ids':ties[:100],'nearest_ties_total':len(ties),'exact_copy':best==0,'near':best<=threshold})
 return {'rows':output,'scales_fitted_from_data':False,'privacy_guaranteed':False,'membership_attack_executed':False}
