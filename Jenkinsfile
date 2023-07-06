node {
    stage ('Build') {
        echo "Setup python environment"
        echo "Activate environment"
        echo "Build the code"
    }

    stage('Test') {
        echo "Runnin tests"
        sh '''
            python3 -m unittest math_functions_test.MathFunctionsTest
        '''
    }  
}