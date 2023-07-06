node {
    stage ('Build') {
        echo "Setup python environment"
        echo "Activate environment"
        echo "Build the code"
    }

    stage('Test') {
        echo "Runnin tests"
        sh '''
            py39
            python -m unittest math_functions_test.MathFunctionsTest
        '''
    }  
}