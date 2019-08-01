
porl = []
porl.clear()
porl_chg_list = []
porl.append(int("116771"))
porl.append(int("-662642"))
porl.append(int("-391430"))
porl.append(int("379920"))
porl.append(int("212354"))
ttl_porl = 0
porl_change = 0
gr_incr = 0
gr_decr = 0
print(porl)

for row in range(len(porl)):
	ttl_porl += porl[row]
	porl_change = porl[row] - porl[row-1]
	print(porl_change)
	#porl_change = porl[row] - prev_porl
	porl_chg_list.append(int(porl_change)) #added int here
	print(porl_chg_list)
	#prev_porl = porl[row]
	if porl_change >= gr_incr:
		gr_incr = porl_change
		#gr_incr_mo = date[row]
		#prev_porl = porl_change
	elif porl_change <= gr_decr:
		gr_decr = porl_change
		#gr_decr_mo = date[row]
		#prev_porl = porl_change
		
ttl_months = len(porl)

sum_of_changes = sum(porl_chg_list)
print(sum_of_changes)
print(ttl_months)
#print(avg)
#avg_chg = round(sum(porl_chg_list)/ttl_months)