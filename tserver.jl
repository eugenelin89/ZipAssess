# To start server, on command line, $julia train.jl

using Pkg
Pkg.activate("env")

using Genie, Genie.Router, Genie.Requests
using Genie.Renderer, Genie.Renderer.Html, Genie.Renderer.Json

println("Load Packages...")
using CSV
using DataFrames
using MLJ

route("/train/:user_id") do
    println("Load CSV...")
    filename = "data_raw/$(payload(:user_id)).csv.clean"
    println(filename)
    df = DataFrame(CSV.File(filename, header=["id", "name","date_time","m1","m2","ans","time","cor"]))
    df_time = df[:, 4:7]
    coerce!(df_time, Count => Continuous);

    println("Training...")
    model = @load LinearRegressor pkg="GLM"
    y, X = unpack(df_time, ==(:time), name->true; rng=123);
    m = machine(model(), X, y)
    train, test = partition(eachindex(y), 0.80, shuffle=true)
    fit!(m, rows=train)
    X12 = DataFrame(m1=Float64[], m2=Float64[], ans=Float64[])
    for i = 1:12
        for j = 1:12
        push!(X12, [float(i), float(j), float(i*j)]) 
        end
    end

    println("Generating Result...")
    pred = predict(m, X12);
    predicted_time = [pred[i].μ for i in 1:size(pred)[1]]  # THIS IS THE RESULT WE WANT
    X12.predicted_time = predicted_time
    sort!(X12, rev=true, [:predicted_time])
    #println(X12)
    #html(X12)
    CSV.write("data_trained/$(payload(:user_id)).trained.csv", X12)
    respond(string(X12), :text)
end

route("/hello.html") do
    html("Hello World")
end

route("/hello.json") do
    json("Hello World")
end

route("/hello.txt") do
    respond("Hello World", :text)
end

up(8001, async = false)