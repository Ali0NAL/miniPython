clear all;

% Constants
filename = 'Bist30.xlsx';
sheet = 1;
range = 'AG:BJ';
pn = 20;
maxiter = 20000;
wmin = 0;
wmax = 0.03;

% Load data
data = xlsread(filename, sheet, range);
yas = numel(data(1, :));

% Initialization
OPT = initializePopulation(pn, yas, wmin, wmax, data);

% Evolutionary optimization
for iter = 1:maxiter
    [bestFitness, bestIndex] = max(OPT(:, yas + 3));
    [worstFitness, worstIndex] = min(OPT(:, yas + 3));

    bestw = OPT(bestIndex, 1:yas);
    worstw = OPT(worstIndex, 1:yas);

    OPT1 = evolvePopulation(pn, yas, OPT, bestw, worstw, data);

    % Update population based on fitness
    for i = 1:pn
        if OPT(i, yas + 3) < OPT1(i, yas + 3)
            OPT(i, :) = OPT1(i, :);
        end
    end
end

% Function to initialize the population
function OPT = initializePopulation(pn, yas, wmin, wmax, data)
    OPT = zeros(pn, yas + 3);

    for i = 1:pn
        w = initializeWeights(yas, wmin, wmax);
        [ER, STSapma, fx] = calculateFitness(w, data, yas);
        OPT(i, 1:yas) = w;
        OPT(i, yas + 1) = ER;
        OPT(i, yas + 2) = STSapma;
        OPT(i, yas + 3) = fx;
    end
end

% Function to initialize weights
function w = initializeWeights(yas, wmin, wmax)
    w = zeros(yas, 1);

    while w(yas) < 0
        for j = 1:yas-1
            w(j) = wmin + rand * (wmax - wmin);
        end
        w(yas) = 1 - sum(w(1:(yas-1)));
    end
end

% Function to calculate fitness
function [ER, STSapma, fx] = calculateFitness(w, data, yas)
    ER = 0;
    for k = 1:yas
        ER = ER + w(k) * mean(data(:, k));
    end

    C = cov(data);
    STD = zeros(yas, 1);

    for st1 = 1:yas
        for st2 = 1:yas
            if st1 == st2
                STD(st1) = STD(st1) + C(st1, st2) * w(st1) * w(st2);
            else
                STD(st1) = STD(st1) + 2 * C(st1, st2) * w(st1) * w(st2);
            end
        end
    end

    STSapma = sqrt(sum(STD));
    fx = ER / STSapma;

    for t = 1:yas
        if w(t) < 0
            fx = -1e-6;
        end
    end
end

% Function to evolve the population
function OPT1 = evolvePopulation(pn, yas, OPT, bestw, worstw, data)
    OPT1 = zeros(pn, yas + 3);

    for i = 1:pn
        w = evolveWeights(OPT(i, 1:yas), bestw, worstw);
        [ER, STSapma, fx] = calculateFitness(w, data, yas);
        OPT1(i, 1:yas) = w;
        OPT1(i, yas + 1) = ER;
        OPT1(i, yas + 2) = STSapma;
        OPT1(i, yas + 3) = fx;
    end
end

% Function to evolve weights
function w = evolveWeights(currentW, bestw, worstw)
    w = currentW;

    for j = 1:numel(currentW) - 1
        w(j) = currentW(j) + rand * (bestw(j) - currentW(j)) - rand * (worstw(j) - currentW(j));

        if w(j) < 0.001
            w(j) = 0;
        end
    end

    w(end) = 1 - sum(w(1:end-1));
end
