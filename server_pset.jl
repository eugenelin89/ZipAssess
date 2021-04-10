using Pkg
Pkg.activate("env")

using Genie, Genie.Router, Genie.Requests
using Genie.Renderer, Genie.Renderer.Html, Genie.Renderer.Json

println("Load Packages...")
using CSV
using DataFrames
using StatsBase
using Random
using JSON

route("/questions/:user_id") do

    filename = "data_trained/$(payload(:user_id)).trained.csv"
    df = DataFrame(CSV.File(filename))
    len = length(df[:,1])
    mid = len ÷ 2
    first_bucket = df[1:mid,:]
    second_bucket = df[mid+1:len,:]
    hard_qs = first_bucket[sample(axes(first_bucket, 1), 15; replace = false, ordered = false), :]
    easy_qs = first_bucket[sample(axes(first_bucket, 1), 5; replace = false, ordered = false), :]
    all_qs = vcat(hard_qs, easy_qs)[:, 1:3]
    all_qs = all_qs[shuffle(1:size(all_qs, 1)),:]

    len = length(all_qs[:,1])
    indices = names(all_qs)

    dic = [Dict([string(index) => Int(all_qs[!,index][i])
                     for index in indices])
               for i in 1:len]
    
    j = JSON.json(dic)

    respond(j, :text)

end

up(8002, async = false)