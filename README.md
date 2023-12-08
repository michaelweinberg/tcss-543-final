# TCSS 543 Final - Group B

## Dicussion of Algorithms

### Preflow Push (Kleinberg and Todos 7.4)

The preflow push (or push relabel) algorithm is another algorithm used to calculate 
maximum flow in a network.  Unlike the ford fulkerson which uses the process of finding 
and augmenting path through the flow network, the preflow push algorithm increases flow
on an edge by edge basis.  Doing this violates the conversation contraints of the flow network. 
The algorithm instead maintains an inequality where the amount of flow entering a node
must be at least as much as the flow exiting a flow.  This inequality can be referred to as the 
excess flow.  In doing this, the preflow push algorithm works towards satisfying conservation constraints
as opoposed to maintaining them at every stage of execution, like in ford-fulkerson.

The algorithm essentially breaks down into 3 phases

1.  The preflow phase
   - Here all heights of all vertices are initialized to 0 except that of the source vertex and 
        all vertices with would receive flow directly from the source will have an excess flow of
        that edge capacity.
2.   The push/relabel phase
   - In this phase, the algorithm works towards turning the preflow into a flow.
   - After the preflow phase, all nodes other than the source have height 0.  The algorithm works to push flow 
     "downhill" to nodes with smaller heights (labels) in our residual graph following the steepness conditions:
     - For all edges (v, w) ∈ Ef in the residual graph, we  have h(v) ≤ h(w) + 1.[^1] 
    -Maintaining this construction insures that starts high from the source node and gradually flow "downhill".
    - the push and relabel phases can be represented in psuedocode as such:

Push Subroutine
```
       push(f, h, v, w) Applicable if ef(v) > 0, h(w) < h(v) and (v, w) ∈ Ef  
        If e = (v, w) is a forward edge then  
            let δ = min(ef(v), ce − f(e)) and  
            increase f(e) by δ  
        If (v, w) is a backward edge then  
            let e = (w, v), δ = min(ef(v), f(e)) and  
            decrease f(e) by δ  
        Return(f, h)
```         
Relabel subroutine
```
    relabel(f, h, v)  
	Applicable if ef(v) > 0, and  
		for all edges (v, w) ∈ Ef we have h(w) ≥ h(v)  
	Increase h(v) by 1  
	Return(f, h) 
```  
[^2]
   - And the full algorithm as such
   - A key concept of this algorithm is 
     that there can be no s-t path in the residual graph.
    
3. Rendering of the max flow
    - once our push/relabel loop has exited, the excess flow of the sink vertex will be 
        equal to the max flow of the network.
Full algorithm
```
   
	Initially h(v) = 0 for all v != s and h(s) = n and  
	f(e) = ce for all e = (s, v) and f(e) = 0 for all other edges  
	While there is a node v != t with excess ef(v) > 0  	Let v be a node with excess  
		If there is w such that push(f, h, v, w) can be applied then  
			push(f, h, v, w) 
		Else  
			relabel(f, h, v)  
	Endwhile  
	Return(f) 
```
[^2]

### Citations:

    -[^1]: Kleinberg, Jon; Tardos, Eva. Algorithm Design (p. 358). Pearson Education. Kindle Edition.
    -[^2]: Kleinberg, Jon; Tardos, Eva. Algorithm Design (p. 360-61). Pearson Education.