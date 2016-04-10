n = #number_of_clusters
for each_cluster in n:
	#Calculate SSE for each_cluster
	for every_other_cluster in n:
		if each_cluster != every_other_cluster:
			#Calculate SSE for each_cluster and every_other_cluster
			#find the smallest cluster and add to a list
			#Repeat for all clusters
			#Once all the clusters are done searching process the list
		end if
	end for
end for
Get the smallest pair - cluster for minimum SSE